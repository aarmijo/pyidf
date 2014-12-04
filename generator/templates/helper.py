import logging
import re


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class DataObject(object):

    def __setitem__(self, key, value):
        key_lower = key.lower()
        if key_lower in self.schema['fields']:
            value = self.check_value(key_lower, value)
            self._data[key_lower] = value
        # TODO extensibles
        else:
            raise ValueError("{} not found in {}".format(key,
                                                         self.schema['pyname']))

    def __getitem__(self, key):
        if isinstance(key, str):
            key_lower = key.lower()
            if key_lower in self.schema['fields']:
                return self._data[key_lower]
        # TODO extensible fields
        raise ValueError("{} not found in {}".format(key,
                                                     self.schema['pyname']))

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        for i, key in enumerate(self.schema['fields']):
            if i < len(vals) and len(vals[i]) == 0:
                self[key] = None
            elif i < len(vals):
                self[key] = vals[i]
        i = len(self.schema['fields'])
        if len(self.schema['extensible-fields']) > 0:
            while i < len(vals):
                ext_vals = [None] * len(self.schema['extensible-fields'])
                for j, val in enumerate(vals[i:i + len(self.schema['extensible-fields'])]):
                    if len(val) == 0:
                        val = None
                    ext_vals[j] = val
                self.add_extensible(*ext_vals)
                i += len(self.schema['extensible-fields'])

        self.strict = old_strict

    def check_value(self, name, value):
        schema = self.schema
        lower_name = name.lower()
        if lower_name in schema['fields']:
            field = schema['fields'][lower_name]
        elif lower_name in schema['extensible-fields']:
            field = schema['extensible-fields'][lower_name]
        else:
            raise ValueError('No field exists with name in data object`{}`'.format(schema['name']))

        if value is not None:
            if field['autocalculatable'] and not field['type'] == "alpha":
                try:
                    value_lower = str(value).lower()
                    if value_lower == "autocalculate":
                        return "Autocalculate"

                    if not self.strict and "auto" in value_lower:
                        logger.warn('Accept value {} as "Autocalculate" '
                                    'for field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                        return "Autocalculate"
                except ValueError:
                    # No string
                    pass

            if field['autosizable'] and not field['type'] == "alpha":
                try:
                    value_lower = str(value).lower()
                    if value_lower == "autosize":
                        return "Autosize"

                    if not self.strict and "auto" in value_lower:
                        logger.warn('Accept value {} as "Autosize" '
                                     'for field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                        return "Autosize"
                except ValueError:
                    pass

            try:
                if field['type'] == "alpha":
                    value = str(value)
                elif field['type'] == "integer":
                    value = int(value)
                elif field['type'] == "real":
                    value = float(value)
                else:
                    value = str(value)
            except ValueError:

                alt = ""
                if field['autosizable']:
                    alt = " or \"Autosize\""
                if field['autocalculatable']:
                    alt = " or \"Autocalculate\""

                if field['type'] == "real":
                    if not self.strict:
                        try:
                            conv_value = int(float(value))
                            logger.warn('Cast float {} to int {}, precision may be lost '
                                         'for field `{}.{}`'.format(value,
                                                                    conv_value,
                                                                    schema['pyname'],
                                                                    field['pyname']))
                            value = conv_value
                        except ValueError:
                            raise ValueError('value {} need to be of type {}{} '
                                             'for field `{}.{}`'.format(value,
                                                                         field['type'],
                                                                         alt,
                                                                         schema['pyname'],
                                                                         field['pyname']))
                else:
                            raise ValueError('value {} need to be of type {}{} '
                                             'for field `{}.{}`'.format(value,
                                                                         field['type'],
                                                                         alt,
                                                                         schema['pyname'],
                                                                         field['pyname']))

            if field['type'] == "alpha":
                if ',' in value:
                    raise ValueError('value should not contain a comma '
                                     'for field `{}.{}`'.format(schema['pyname'],
                                                                field['pyname']))
                if '!' in value:
                    raise ValueError('value should not contain a ! '
                                     'for field `{}.{}`'.format(schema['pyname'],
                                                                field['pyname']))
            else:

                if 'minimum' in field and value < field['minimum']:
                    raise ValueError('value {} need to be greater or equal {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['minimum'],
                                                                schema['pyname'],
                                                                field['pyname']))

                if 'minimum>' in field and value <= field['minimum>']:
                    raise ValueError('value {} need to be greater  {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['minimum>'],
                                                                schema['pyname'],
                                                                field['pyname']))

                if 'maximum' in field and value > field['maximum']:
                    raise ValueError('value {} need to be smaller or equal  {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['maximum'],
                                                                schema['pyname'],
                                                                field['pyname']))
                if 'maximum<' in field and value >= field['maximum<']:
                    raise ValueError('value {} need to be smaller  {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['maximum<'],
                                                                schema['pyname'],
                                                                field['pyname']))

            if 'accepted-values' in field:
                vals = set(field['accepted-values'])

                if field['type'] == "alpha":
                    value_lower = value.lower()
                else:
                    value_lower = value

                if value_lower not in vals:
                    found = False
                    if not self.strict:
                        for key in vals:
                            if key in value_lower or value_lower in key:
                                value_lower = key
                                found = True
                                break
                        if not found:
                            value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                            for key in vals:
                                key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                                if key_stripped == value_stripped:
                                    value_lower = key
                                    found = True
                                    break
                    if not found:
                        raise ValueError('value {} is not an accepted value for '
                                         'field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                    else:
                        logger.warn('change value {} to accepted value {} for '
                                    'field `{}.{}`'.format(value,
                                                           vals[value_lower],
                                                           schema['pyname'],
                                                           field['pyname']))
                value = value_lower

        # value is None
        else:
            if 'required-field' in field and 'default' in field:
                key = field['name'].lower()
                if key in self.schema['fields'] and self.schema['fields'].keys().index(key) < self.schema['min-fields']:
                    logger.warn('Replacing None value for required field `{}.{}` '
                                'with {}'.format(schema['pyname'],
                                                 field['pyname'],
                                                 field['default']))
                value = field['default']

        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key, field in self.schema['fields'].iteritems():
            if field['required-field'] and self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field {}.{} is None".format(key,
                                                                           self.schema['pyname'],
                                                                           self.field['pyname']))
                    break
                else:
                    logger.warn("Required field {}:{} is None".format(key,
                                                                     self.schema['pyname'],
                                                                     self.field['pyname']))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.schema['min-fields']
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for {}: {} / {}".format(self.schema['pyname'],
                                                                            out_fields,
                                                                            self.schema['min-fields']))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for {}: {} / {}".format(self.schema['pyname'],
                                                                       out_fields,
                                                                       self.schema['min-fields']))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            maxel = 0
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                if self._data[key] is not None:
                    maxel = i + 1
                    break

        maxel = max(maxel, self.schema['min-fields'])

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.schema['extensible-fields'].keys()[i], self._to_str(value)))
        return out

    def __str__(self):
        out = self.export()
        string = ",".join([self.schema['name']] + [o[1] for o in out])
        if len(string) > 77:
            string = string[:77] + "..."
        return string

    def __iter__(self):
        for val in self._data.values():
            yield val

class DONames:
    {%- for obj in objs %}
    {{ obj.class_name }} = "{{ obj.internal_name }}"
    {%- endfor %}