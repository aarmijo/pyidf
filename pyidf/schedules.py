from collections import OrderedDict

class ScheduleTypeLimits(object):
    """ Corresponds to IDD object `ScheduleTypeLimits`
        ScheduleTypeLimits specifies the data types and limits for the values contained in schedules
    """
    internal_name = "ScheduleTypeLimits"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `ScheduleTypeLimits`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Lower Limit Value"] = None
        self._data["Upper Limit Value"] = None
        self._data["Numeric Type"] = None
        self._data["Unit Type"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lower_limit_value = None
        else:
            self.lower_limit_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.upper_limit_value = None
        else:
            self.upper_limit_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.numeric_type = None
        else:
            self.numeric_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unit_type = None
        else:
            self.unit_type = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        used to validate schedule types in various schedule objects

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def lower_limit_value(self):
        """Get lower_limit_value

        Returns:
            float: the value of `lower_limit_value` or None if not set
        """
        return self._data["Lower Limit Value"]

    @lower_limit_value.setter
    def lower_limit_value(self, value=None):
        """  Corresponds to IDD Field `lower_limit_value`
        lower limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 0.0

        Args:
            value (float): value for IDD Field `lower_limit_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `lower_limit_value`'.format(value))

        self._data["Lower Limit Value"] = value

    @property
    def upper_limit_value(self):
        """Get upper_limit_value

        Returns:
            float: the value of `upper_limit_value` or None if not set
        """
        return self._data["Upper Limit Value"]

    @upper_limit_value.setter
    def upper_limit_value(self, value=None):
        """  Corresponds to IDD Field `upper_limit_value`
        upper limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 1.0

        Args:
            value (float): value for IDD Field `upper_limit_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `upper_limit_value`'.format(value))

        self._data["Upper Limit Value"] = value

    @property
    def numeric_type(self):
        """Get numeric_type

        Returns:
            str: the value of `numeric_type` or None if not set
        """
        return self._data["Numeric Type"]

    @numeric_type.setter
    def numeric_type(self, value=None):
        """  Corresponds to IDD Field `numeric_type`
        Numeric type is either Continuous (all numbers within the min and
        max are valid or Discrete (only integer numbers between min and
        max are valid.  (Could also allow REAL and INTEGER to mean the
        same things)

        Args:
            value (str): value for IDD Field `numeric_type`
                Accepted values are:
                      - Continuous
                      - Discrete
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `numeric_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `numeric_type`')
            vals = set()
            vals.add("Continuous")
            vals.add("Discrete")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `numeric_type`'.format(value))

        self._data["Numeric Type"] = value

    @property
    def unit_type(self):
        """Get unit_type

        Returns:
            str: the value of `unit_type` or None if not set
        """
        return self._data["Unit Type"]

    @unit_type.setter
    def unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `unit_type`
        Temperature (C or F)
        DeltaTemperature (C or F)
        PrecipitationRate (m/hr or ft/hr)
        Angle (degrees)
        Convection Coefficient (W/m2-K or Btu/sqft-hr-F)
        Activity Level (W/person)
        Velocity (m/s or ft/min)
        Capacity (W or Btu/h)
        Power (W)

        Args:
            value (str): value for IDD Field `unit_type`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - DeltaTemperature
                      - PrecipitationRate
                      - Angle
                      - ConvectionCoefficient
                      - ActivityLevel
                      - Velocity
                      - Capacity
                      - Power
                      - Availability
                      - Percent
                      - Control
                      - Mode
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unit_type`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("DeltaTemperature")
            vals.add("PrecipitationRate")
            vals.add("Angle")
            vals.add("ConvectionCoefficient")
            vals.add("ActivityLevel")
            vals.add("Velocity")
            vals.add("Capacity")
            vals.add("Power")
            vals.add("Availability")
            vals.add("Percent")
            vals.add("Control")
            vals.add("Mode")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `unit_type`'.format(value))

        self._data["Unit Type"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.lower_limit_value))
        out.append(self._to_str(self.upper_limit_value))
        out.append(self._to_str(self.numeric_type))
        out.append(self._to_str(self.unit_type))
        return ",".join(out)

class ScheduleDayHourly(object):
    """ Corresponds to IDD object `Schedule:Day:Hourly`
        A Schedule:Day:Hourly contains 24 values for each hour of the day.
    """
    internal_name = "Schedule:Day:Hourly"
    field_count = 26

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Day:Hourly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Hour 1"] = None
        self._data["Hour 2"] = None
        self._data["Hour 3"] = None
        self._data["Hour 4"] = None
        self._data["Hour 5"] = None
        self._data["Hour 6"] = None
        self._data["Hour 7"] = None
        self._data["Hour 8"] = None
        self._data["Hour 9"] = None
        self._data["Hour 10"] = None
        self._data["Hour 11"] = None
        self._data["Hour 12"] = None
        self._data["Hour 13"] = None
        self._data["Hour 14"] = None
        self._data["Hour 15"] = None
        self._data["Hour 16"] = None
        self._data["Hour 17"] = None
        self._data["Hour 18"] = None
        self._data["Hour 19"] = None
        self._data["Hour 20"] = None
        self._data["Hour 21"] = None
        self._data["Hour 22"] = None
        self._data["Hour 23"] = None
        self._data["Hour 24"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_1 = None
        else:
            self.hour_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_2 = None
        else:
            self.hour_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_3 = None
        else:
            self.hour_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_4 = None
        else:
            self.hour_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_5 = None
        else:
            self.hour_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_6 = None
        else:
            self.hour_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_7 = None
        else:
            self.hour_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_8 = None
        else:
            self.hour_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_9 = None
        else:
            self.hour_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_10 = None
        else:
            self.hour_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_11 = None
        else:
            self.hour_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_12 = None
        else:
            self.hour_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_13 = None
        else:
            self.hour_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_14 = None
        else:
            self.hour_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_15 = None
        else:
            self.hour_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_16 = None
        else:
            self.hour_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_17 = None
        else:
            self.hour_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_18 = None
        else:
            self.hour_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_19 = None
        else:
            self.hour_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_20 = None
        else:
            self.hour_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_21 = None
        else:
            self.hour_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_22 = None
        else:
            self.hour_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_23 = None
        else:
            self.hour_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour_24 = None
        else:
            self.hour_24 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_name`

        Args:
            value (str): value for IDD Field `schedule_type_limits_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_name`')

        self._data["Schedule Type Limits Name"] = value

    @property
    def hour_1(self):
        """Get hour_1

        Returns:
            float: the value of `hour_1` or None if not set
        """
        return self._data["Hour 1"]

    @hour_1.setter
    def hour_1(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_1`

        Args:
            value (float): value for IDD Field `hour_1`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_1`'.format(value))

        self._data["Hour 1"] = value

    @property
    def hour_2(self):
        """Get hour_2

        Returns:
            float: the value of `hour_2` or None if not set
        """
        return self._data["Hour 2"]

    @hour_2.setter
    def hour_2(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_2`

        Args:
            value (float): value for IDD Field `hour_2`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_2`'.format(value))

        self._data["Hour 2"] = value

    @property
    def hour_3(self):
        """Get hour_3

        Returns:
            float: the value of `hour_3` or None if not set
        """
        return self._data["Hour 3"]

    @hour_3.setter
    def hour_3(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_3`

        Args:
            value (float): value for IDD Field `hour_3`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_3`'.format(value))

        self._data["Hour 3"] = value

    @property
    def hour_4(self):
        """Get hour_4

        Returns:
            float: the value of `hour_4` or None if not set
        """
        return self._data["Hour 4"]

    @hour_4.setter
    def hour_4(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_4`

        Args:
            value (float): value for IDD Field `hour_4`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_4`'.format(value))

        self._data["Hour 4"] = value

    @property
    def hour_5(self):
        """Get hour_5

        Returns:
            float: the value of `hour_5` or None if not set
        """
        return self._data["Hour 5"]

    @hour_5.setter
    def hour_5(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_5`

        Args:
            value (float): value for IDD Field `hour_5`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_5`'.format(value))

        self._data["Hour 5"] = value

    @property
    def hour_6(self):
        """Get hour_6

        Returns:
            float: the value of `hour_6` or None if not set
        """
        return self._data["Hour 6"]

    @hour_6.setter
    def hour_6(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_6`

        Args:
            value (float): value for IDD Field `hour_6`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_6`'.format(value))

        self._data["Hour 6"] = value

    @property
    def hour_7(self):
        """Get hour_7

        Returns:
            float: the value of `hour_7` or None if not set
        """
        return self._data["Hour 7"]

    @hour_7.setter
    def hour_7(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_7`

        Args:
            value (float): value for IDD Field `hour_7`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_7`'.format(value))

        self._data["Hour 7"] = value

    @property
    def hour_8(self):
        """Get hour_8

        Returns:
            float: the value of `hour_8` or None if not set
        """
        return self._data["Hour 8"]

    @hour_8.setter
    def hour_8(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_8`

        Args:
            value (float): value for IDD Field `hour_8`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_8`'.format(value))

        self._data["Hour 8"] = value

    @property
    def hour_9(self):
        """Get hour_9

        Returns:
            float: the value of `hour_9` or None if not set
        """
        return self._data["Hour 9"]

    @hour_9.setter
    def hour_9(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_9`

        Args:
            value (float): value for IDD Field `hour_9`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_9`'.format(value))

        self._data["Hour 9"] = value

    @property
    def hour_10(self):
        """Get hour_10

        Returns:
            float: the value of `hour_10` or None if not set
        """
        return self._data["Hour 10"]

    @hour_10.setter
    def hour_10(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_10`

        Args:
            value (float): value for IDD Field `hour_10`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_10`'.format(value))

        self._data["Hour 10"] = value

    @property
    def hour_11(self):
        """Get hour_11

        Returns:
            float: the value of `hour_11` or None if not set
        """
        return self._data["Hour 11"]

    @hour_11.setter
    def hour_11(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_11`

        Args:
            value (float): value for IDD Field `hour_11`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_11`'.format(value))

        self._data["Hour 11"] = value

    @property
    def hour_12(self):
        """Get hour_12

        Returns:
            float: the value of `hour_12` or None if not set
        """
        return self._data["Hour 12"]

    @hour_12.setter
    def hour_12(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_12`

        Args:
            value (float): value for IDD Field `hour_12`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_12`'.format(value))

        self._data["Hour 12"] = value

    @property
    def hour_13(self):
        """Get hour_13

        Returns:
            float: the value of `hour_13` or None if not set
        """
        return self._data["Hour 13"]

    @hour_13.setter
    def hour_13(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_13`

        Args:
            value (float): value for IDD Field `hour_13`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_13`'.format(value))

        self._data["Hour 13"] = value

    @property
    def hour_14(self):
        """Get hour_14

        Returns:
            float: the value of `hour_14` or None if not set
        """
        return self._data["Hour 14"]

    @hour_14.setter
    def hour_14(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_14`

        Args:
            value (float): value for IDD Field `hour_14`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_14`'.format(value))

        self._data["Hour 14"] = value

    @property
    def hour_15(self):
        """Get hour_15

        Returns:
            float: the value of `hour_15` or None if not set
        """
        return self._data["Hour 15"]

    @hour_15.setter
    def hour_15(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_15`

        Args:
            value (float): value for IDD Field `hour_15`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_15`'.format(value))

        self._data["Hour 15"] = value

    @property
    def hour_16(self):
        """Get hour_16

        Returns:
            float: the value of `hour_16` or None if not set
        """
        return self._data["Hour 16"]

    @hour_16.setter
    def hour_16(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_16`

        Args:
            value (float): value for IDD Field `hour_16`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_16`'.format(value))

        self._data["Hour 16"] = value

    @property
    def hour_17(self):
        """Get hour_17

        Returns:
            float: the value of `hour_17` or None if not set
        """
        return self._data["Hour 17"]

    @hour_17.setter
    def hour_17(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_17`

        Args:
            value (float): value for IDD Field `hour_17`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_17`'.format(value))

        self._data["Hour 17"] = value

    @property
    def hour_18(self):
        """Get hour_18

        Returns:
            float: the value of `hour_18` or None if not set
        """
        return self._data["Hour 18"]

    @hour_18.setter
    def hour_18(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_18`

        Args:
            value (float): value for IDD Field `hour_18`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_18`'.format(value))

        self._data["Hour 18"] = value

    @property
    def hour_19(self):
        """Get hour_19

        Returns:
            float: the value of `hour_19` or None if not set
        """
        return self._data["Hour 19"]

    @hour_19.setter
    def hour_19(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_19`

        Args:
            value (float): value for IDD Field `hour_19`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_19`'.format(value))

        self._data["Hour 19"] = value

    @property
    def hour_20(self):
        """Get hour_20

        Returns:
            float: the value of `hour_20` or None if not set
        """
        return self._data["Hour 20"]

    @hour_20.setter
    def hour_20(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_20`

        Args:
            value (float): value for IDD Field `hour_20`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_20`'.format(value))

        self._data["Hour 20"] = value

    @property
    def hour_21(self):
        """Get hour_21

        Returns:
            float: the value of `hour_21` or None if not set
        """
        return self._data["Hour 21"]

    @hour_21.setter
    def hour_21(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_21`

        Args:
            value (float): value for IDD Field `hour_21`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_21`'.format(value))

        self._data["Hour 21"] = value

    @property
    def hour_22(self):
        """Get hour_22

        Returns:
            float: the value of `hour_22` or None if not set
        """
        return self._data["Hour 22"]

    @hour_22.setter
    def hour_22(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_22`

        Args:
            value (float): value for IDD Field `hour_22`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_22`'.format(value))

        self._data["Hour 22"] = value

    @property
    def hour_23(self):
        """Get hour_23

        Returns:
            float: the value of `hour_23` or None if not set
        """
        return self._data["Hour 23"]

    @hour_23.setter
    def hour_23(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_23`

        Args:
            value (float): value for IDD Field `hour_23`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_23`'.format(value))

        self._data["Hour 23"] = value

    @property
    def hour_24(self):
        """Get hour_24

        Returns:
            float: the value of `hour_24` or None if not set
        """
        return self._data["Hour 24"]

    @hour_24.setter
    def hour_24(self, value=0.0 ):
        """  Corresponds to IDD Field `hour_24`

        Args:
            value (float): value for IDD Field `hour_24`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hour_24`'.format(value))

        self._data["Hour 24"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_type_limits_name))
        out.append(self._to_str(self.hour_1))
        out.append(self._to_str(self.hour_2))
        out.append(self._to_str(self.hour_3))
        out.append(self._to_str(self.hour_4))
        out.append(self._to_str(self.hour_5))
        out.append(self._to_str(self.hour_6))
        out.append(self._to_str(self.hour_7))
        out.append(self._to_str(self.hour_8))
        out.append(self._to_str(self.hour_9))
        out.append(self._to_str(self.hour_10))
        out.append(self._to_str(self.hour_11))
        out.append(self._to_str(self.hour_12))
        out.append(self._to_str(self.hour_13))
        out.append(self._to_str(self.hour_14))
        out.append(self._to_str(self.hour_15))
        out.append(self._to_str(self.hour_16))
        out.append(self._to_str(self.hour_17))
        out.append(self._to_str(self.hour_18))
        out.append(self._to_str(self.hour_19))
        out.append(self._to_str(self.hour_20))
        out.append(self._to_str(self.hour_21))
        out.append(self._to_str(self.hour_22))
        out.append(self._to_str(self.hour_23))
        out.append(self._to_str(self.hour_24))
        return ",".join(out)

class ScheduleDayInterval(object):
    """ Corresponds to IDD object `Schedule:Day:Interval`
        A Schedule:Day:Interval contains a full day of values with specified end times for each value
        Currently, is set up to allow for 10 minute intervals for an entire day.
    """
    internal_name = "Schedule:Day:Interval"
    field_count = 291

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Day:Interval`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Interpolate to Timestep"] = None
        self._data["Time 1"] = None
        self._data["Value Until Time 1"] = None
        self._data["Time 2"] = None
        self._data["Value Until Time 2"] = None
        self._data["Time 3"] = None
        self._data["Value Until Time 3"] = None
        self._data["Time 4"] = None
        self._data["Value Until Time 4"] = None
        self._data["Time 5"] = None
        self._data["Value Until Time 5"] = None
        self._data["Time 6"] = None
        self._data["Value Until Time 6"] = None
        self._data["Time 7"] = None
        self._data["Value Until Time 7"] = None
        self._data["Time 8"] = None
        self._data["Value Until Time 8"] = None
        self._data["Time 9"] = None
        self._data["Value Until Time 9"] = None
        self._data["Time 10"] = None
        self._data["Value Until Time 10"] = None
        self._data["Time 11"] = None
        self._data["Value Until Time 11"] = None
        self._data["Time 12"] = None
        self._data["Value Until Time 12"] = None
        self._data["Time 13"] = None
        self._data["Value Until Time 13"] = None
        self._data["Time 14"] = None
        self._data["Value Until Time 14"] = None
        self._data["Time 15"] = None
        self._data["Value Until Time 15"] = None
        self._data["Time 16"] = None
        self._data["Value Until Time 16"] = None
        self._data["Time 17"] = None
        self._data["Value Until Time 17"] = None
        self._data["Time 18"] = None
        self._data["Value Until Time 18"] = None
        self._data["Time 19"] = None
        self._data["Value Until Time 19"] = None
        self._data["Time 20"] = None
        self._data["Value Until Time 20"] = None
        self._data["Time 21"] = None
        self._data["Value Until Time 21"] = None
        self._data["Time 22"] = None
        self._data["Value Until Time 22"] = None
        self._data["Time 23"] = None
        self._data["Value Until Time 23"] = None
        self._data["Time 24"] = None
        self._data["Value Until Time 24"] = None
        self._data["Time 25"] = None
        self._data["Value Until Time 25"] = None
        self._data["Time 26"] = None
        self._data["Value Until Time 26"] = None
        self._data["Time 27"] = None
        self._data["Value Until Time 27"] = None
        self._data["Time 28"] = None
        self._data["Value Until Time 28"] = None
        self._data["Time 29"] = None
        self._data["Value Until Time 29"] = None
        self._data["Time 30"] = None
        self._data["Value Until Time 30"] = None
        self._data["Time 31"] = None
        self._data["Value Until Time 31"] = None
        self._data["Time 32"] = None
        self._data["Value Until Time 32"] = None
        self._data["Time 33"] = None
        self._data["Value Until Time 33"] = None
        self._data["Time 34"] = None
        self._data["Value Until Time 34"] = None
        self._data["Time 35"] = None
        self._data["Value Until Time 35"] = None
        self._data["Time 36"] = None
        self._data["Value Until Time 36"] = None
        self._data["Time 37"] = None
        self._data["Value Until Time 37"] = None
        self._data["Time 38"] = None
        self._data["Value Until Time 38"] = None
        self._data["Time 39"] = None
        self._data["Value Until Time 39"] = None
        self._data["Time 40"] = None
        self._data["Value Until Time 40"] = None
        self._data["Time 41"] = None
        self._data["Value Until Time 41"] = None
        self._data["Time 42"] = None
        self._data["Value Until Time 42"] = None
        self._data["Time 43"] = None
        self._data["Value Until Time 43"] = None
        self._data["Time 44"] = None
        self._data["Value Until Time 44"] = None
        self._data["Time 45"] = None
        self._data["Value Until Time 45"] = None
        self._data["Time 46"] = None
        self._data["Value Until Time 46"] = None
        self._data["Time 47"] = None
        self._data["Value Until Time 47"] = None
        self._data["Time 48"] = None
        self._data["Value Until Time 48"] = None
        self._data["Time 49"] = None
        self._data["Value Until Time 49"] = None
        self._data["Time 50"] = None
        self._data["Value Until Time 50"] = None
        self._data["Time 51"] = None
        self._data["Value Until Time 51"] = None
        self._data["Time 52"] = None
        self._data["Value Until Time 52"] = None
        self._data["Time 53"] = None
        self._data["Value Until Time 53"] = None
        self._data["Time 54"] = None
        self._data["Value Until Time 54"] = None
        self._data["Time 55"] = None
        self._data["Value Until Time 55"] = None
        self._data["Time 56"] = None
        self._data["Value Until Time 56"] = None
        self._data["Time 57"] = None
        self._data["Value Until Time 57"] = None
        self._data["Time 58"] = None
        self._data["Value Until Time 58"] = None
        self._data["Time 59"] = None
        self._data["Value Until Time 59"] = None
        self._data["Time 60"] = None
        self._data["Value Until Time 60"] = None
        self._data["Time 61"] = None
        self._data["Value Until Time 61"] = None
        self._data["Time 62"] = None
        self._data["Value Until Time 62"] = None
        self._data["Time 63"] = None
        self._data["Value Until Time 63"] = None
        self._data["Time 64"] = None
        self._data["Value Until Time 64"] = None
        self._data["Time 65"] = None
        self._data["Value Until Time 65"] = None
        self._data["Time 66"] = None
        self._data["Value Until Time 66"] = None
        self._data["Time 67"] = None
        self._data["Value Until Time 67"] = None
        self._data["Time 68"] = None
        self._data["Value Until Time 68"] = None
        self._data["Time 69"] = None
        self._data["Value Until Time 69"] = None
        self._data["Time 70"] = None
        self._data["Value Until Time 70"] = None
        self._data["Time 71"] = None
        self._data["Value Until Time 71"] = None
        self._data["Time 72"] = None
        self._data["Value Until Time 72"] = None
        self._data["Time 73"] = None
        self._data["Value Until Time 73"] = None
        self._data["Time 74"] = None
        self._data["Value Until Time 74"] = None
        self._data["Time 75"] = None
        self._data["Value Until Time 75"] = None
        self._data["Time 76"] = None
        self._data["Value Until Time 76"] = None
        self._data["Time 77"] = None
        self._data["Value Until Time 77"] = None
        self._data["Time 78"] = None
        self._data["Value Until Time 78"] = None
        self._data["Time 79"] = None
        self._data["Value Until Time 79"] = None
        self._data["Time 80"] = None
        self._data["Value Until Time 80"] = None
        self._data["Time 81"] = None
        self._data["Value Until Time 81"] = None
        self._data["Time 82"] = None
        self._data["Value Until Time 82"] = None
        self._data["Time 83"] = None
        self._data["Value Until Time 83"] = None
        self._data["Time 84"] = None
        self._data["Value Until Time 84"] = None
        self._data["Time 85"] = None
        self._data["Value Until Time 85"] = None
        self._data["Time 86"] = None
        self._data["Value Until Time 86"] = None
        self._data["Time 87"] = None
        self._data["Value Until Time 87"] = None
        self._data["Time 88"] = None
        self._data["Value Until Time 88"] = None
        self._data["Time 89"] = None
        self._data["Value Until Time 89"] = None
        self._data["Time 90"] = None
        self._data["Value Until Time 90"] = None
        self._data["Time 91"] = None
        self._data["Value Until Time 91"] = None
        self._data["Time 92"] = None
        self._data["Value Until Time 92"] = None
        self._data["Time 93"] = None
        self._data["Value Until Time 93"] = None
        self._data["Time 94"] = None
        self._data["Value Until Time 94"] = None
        self._data["Time 95"] = None
        self._data["Value Until Time 95"] = None
        self._data["Time 96"] = None
        self._data["Value Until Time 96"] = None
        self._data["Time 97"] = None
        self._data["Value Until Time 97"] = None
        self._data["Time 98"] = None
        self._data["Value Until Time 98"] = None
        self._data["Time 99"] = None
        self._data["Value Until Time 99"] = None
        self._data["Time 100"] = None
        self._data["Value Until Time 100"] = None
        self._data["Time 101"] = None
        self._data["Value Until Time 101"] = None
        self._data["Time 102"] = None
        self._data["Value Until Time 102"] = None
        self._data["Time 103"] = None
        self._data["Value Until Time 103"] = None
        self._data["Time 104"] = None
        self._data["Value Until Time 104"] = None
        self._data["Time 105"] = None
        self._data["Value Until Time 105"] = None
        self._data["Time 106"] = None
        self._data["Value Until Time 106"] = None
        self._data["Time 107"] = None
        self._data["Value Until Time 107"] = None
        self._data["Time 108"] = None
        self._data["Value Until Time 108"] = None
        self._data["Time 109"] = None
        self._data["Value Until Time 109"] = None
        self._data["Time 110"] = None
        self._data["Value Until Time 110"] = None
        self._data["Time 111"] = None
        self._data["Value Until Time 111"] = None
        self._data["Time 112"] = None
        self._data["Value Until Time 112"] = None
        self._data["Time 113"] = None
        self._data["Value Until Time 113"] = None
        self._data["Time 114"] = None
        self._data["Value Until Time 114"] = None
        self._data["Time 115"] = None
        self._data["Value Until Time 115"] = None
        self._data["Time 116"] = None
        self._data["Value Until Time 116"] = None
        self._data["Time 117"] = None
        self._data["Value Until Time 117"] = None
        self._data["Time 118"] = None
        self._data["Value Until Time 118"] = None
        self._data["Time 119"] = None
        self._data["Value Until Time 119"] = None
        self._data["Time 120"] = None
        self._data["Value Until Time 120"] = None
        self._data["Time 121"] = None
        self._data["Value Until Time 121"] = None
        self._data["Time 122"] = None
        self._data["Value Until Time 122"] = None
        self._data["Time 123"] = None
        self._data["Value Until Time 123"] = None
        self._data["Time 124"] = None
        self._data["Value Until Time 124"] = None
        self._data["Time 125"] = None
        self._data["Value Until Time 125"] = None
        self._data["Time 126"] = None
        self._data["Value Until Time 126"] = None
        self._data["Time 127"] = None
        self._data["Value Until Time 127"] = None
        self._data["Time 128"] = None
        self._data["Value Until Time 128"] = None
        self._data["Time 129"] = None
        self._data["Value Until Time 129"] = None
        self._data["Time 130"] = None
        self._data["Value Until Time 130"] = None
        self._data["Time 131"] = None
        self._data["Value Until Time 131"] = None
        self._data["Time 132"] = None
        self._data["Value Until Time 132"] = None
        self._data["Time 133"] = None
        self._data["Value Until Time 133"] = None
        self._data["Time 134"] = None
        self._data["Value Until Time 134"] = None
        self._data["Time 135"] = None
        self._data["Value Until Time 135"] = None
        self._data["Time 136"] = None
        self._data["Value Until Time 136"] = None
        self._data["Time 137"] = None
        self._data["Value Until Time 137"] = None
        self._data["Time 138"] = None
        self._data["Value Until Time 138"] = None
        self._data["Time 139"] = None
        self._data["Value Until Time 139"] = None
        self._data["Time 140"] = None
        self._data["Value Until Time 140"] = None
        self._data["Time 141"] = None
        self._data["Value Until Time 141"] = None
        self._data["Time 142"] = None
        self._data["Value Until Time 142"] = None
        self._data["Time 143"] = None
        self._data["Value Until Time 143"] = None
        self._data["Time 144"] = None
        self._data["Value Until Time 144"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.interpolate_to_timestep = None
        else:
            self.interpolate_to_timestep = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_1 = None
        else:
            self.time_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_1 = None
        else:
            self.value_until_time_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_2 = None
        else:
            self.time_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_2 = None
        else:
            self.value_until_time_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_3 = None
        else:
            self.time_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_3 = None
        else:
            self.value_until_time_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_4 = None
        else:
            self.time_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_4 = None
        else:
            self.value_until_time_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_5 = None
        else:
            self.time_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_5 = None
        else:
            self.value_until_time_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_6 = None
        else:
            self.time_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_6 = None
        else:
            self.value_until_time_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_7 = None
        else:
            self.time_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_7 = None
        else:
            self.value_until_time_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_8 = None
        else:
            self.time_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_8 = None
        else:
            self.value_until_time_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_9 = None
        else:
            self.time_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_9 = None
        else:
            self.value_until_time_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_10 = None
        else:
            self.time_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_10 = None
        else:
            self.value_until_time_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_11 = None
        else:
            self.time_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_11 = None
        else:
            self.value_until_time_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_12 = None
        else:
            self.time_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_12 = None
        else:
            self.value_until_time_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_13 = None
        else:
            self.time_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_13 = None
        else:
            self.value_until_time_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_14 = None
        else:
            self.time_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_14 = None
        else:
            self.value_until_time_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_15 = None
        else:
            self.time_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_15 = None
        else:
            self.value_until_time_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_16 = None
        else:
            self.time_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_16 = None
        else:
            self.value_until_time_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_17 = None
        else:
            self.time_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_17 = None
        else:
            self.value_until_time_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_18 = None
        else:
            self.time_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_18 = None
        else:
            self.value_until_time_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_19 = None
        else:
            self.time_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_19 = None
        else:
            self.value_until_time_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_20 = None
        else:
            self.time_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_20 = None
        else:
            self.value_until_time_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_21 = None
        else:
            self.time_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_21 = None
        else:
            self.value_until_time_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_22 = None
        else:
            self.time_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_22 = None
        else:
            self.value_until_time_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_23 = None
        else:
            self.time_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_23 = None
        else:
            self.value_until_time_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_24 = None
        else:
            self.time_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_24 = None
        else:
            self.value_until_time_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_25 = None
        else:
            self.time_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_25 = None
        else:
            self.value_until_time_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_26 = None
        else:
            self.time_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_26 = None
        else:
            self.value_until_time_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_27 = None
        else:
            self.time_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_27 = None
        else:
            self.value_until_time_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_28 = None
        else:
            self.time_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_28 = None
        else:
            self.value_until_time_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_29 = None
        else:
            self.time_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_29 = None
        else:
            self.value_until_time_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_30 = None
        else:
            self.time_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_30 = None
        else:
            self.value_until_time_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_31 = None
        else:
            self.time_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_31 = None
        else:
            self.value_until_time_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_32 = None
        else:
            self.time_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_32 = None
        else:
            self.value_until_time_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_33 = None
        else:
            self.time_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_33 = None
        else:
            self.value_until_time_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_34 = None
        else:
            self.time_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_34 = None
        else:
            self.value_until_time_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_35 = None
        else:
            self.time_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_35 = None
        else:
            self.value_until_time_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_36 = None
        else:
            self.time_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_36 = None
        else:
            self.value_until_time_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_37 = None
        else:
            self.time_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_37 = None
        else:
            self.value_until_time_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_38 = None
        else:
            self.time_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_38 = None
        else:
            self.value_until_time_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_39 = None
        else:
            self.time_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_39 = None
        else:
            self.value_until_time_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_40 = None
        else:
            self.time_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_40 = None
        else:
            self.value_until_time_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_41 = None
        else:
            self.time_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_41 = None
        else:
            self.value_until_time_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_42 = None
        else:
            self.time_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_42 = None
        else:
            self.value_until_time_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_43 = None
        else:
            self.time_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_43 = None
        else:
            self.value_until_time_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_44 = None
        else:
            self.time_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_44 = None
        else:
            self.value_until_time_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_45 = None
        else:
            self.time_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_45 = None
        else:
            self.value_until_time_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_46 = None
        else:
            self.time_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_46 = None
        else:
            self.value_until_time_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_47 = None
        else:
            self.time_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_47 = None
        else:
            self.value_until_time_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_48 = None
        else:
            self.time_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_48 = None
        else:
            self.value_until_time_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_49 = None
        else:
            self.time_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_49 = None
        else:
            self.value_until_time_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_50 = None
        else:
            self.time_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_50 = None
        else:
            self.value_until_time_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_51 = None
        else:
            self.time_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_51 = None
        else:
            self.value_until_time_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_52 = None
        else:
            self.time_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_52 = None
        else:
            self.value_until_time_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_53 = None
        else:
            self.time_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_53 = None
        else:
            self.value_until_time_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_54 = None
        else:
            self.time_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_54 = None
        else:
            self.value_until_time_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_55 = None
        else:
            self.time_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_55 = None
        else:
            self.value_until_time_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_56 = None
        else:
            self.time_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_56 = None
        else:
            self.value_until_time_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_57 = None
        else:
            self.time_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_57 = None
        else:
            self.value_until_time_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_58 = None
        else:
            self.time_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_58 = None
        else:
            self.value_until_time_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_59 = None
        else:
            self.time_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_59 = None
        else:
            self.value_until_time_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_60 = None
        else:
            self.time_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_60 = None
        else:
            self.value_until_time_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_61 = None
        else:
            self.time_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_61 = None
        else:
            self.value_until_time_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_62 = None
        else:
            self.time_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_62 = None
        else:
            self.value_until_time_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_63 = None
        else:
            self.time_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_63 = None
        else:
            self.value_until_time_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_64 = None
        else:
            self.time_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_64 = None
        else:
            self.value_until_time_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_65 = None
        else:
            self.time_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_65 = None
        else:
            self.value_until_time_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_66 = None
        else:
            self.time_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_66 = None
        else:
            self.value_until_time_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_67 = None
        else:
            self.time_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_67 = None
        else:
            self.value_until_time_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_68 = None
        else:
            self.time_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_68 = None
        else:
            self.value_until_time_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_69 = None
        else:
            self.time_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_69 = None
        else:
            self.value_until_time_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_70 = None
        else:
            self.time_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_70 = None
        else:
            self.value_until_time_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_71 = None
        else:
            self.time_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_71 = None
        else:
            self.value_until_time_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_72 = None
        else:
            self.time_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_72 = None
        else:
            self.value_until_time_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_73 = None
        else:
            self.time_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_73 = None
        else:
            self.value_until_time_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_74 = None
        else:
            self.time_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_74 = None
        else:
            self.value_until_time_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_75 = None
        else:
            self.time_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_75 = None
        else:
            self.value_until_time_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_76 = None
        else:
            self.time_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_76 = None
        else:
            self.value_until_time_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_77 = None
        else:
            self.time_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_77 = None
        else:
            self.value_until_time_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_78 = None
        else:
            self.time_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_78 = None
        else:
            self.value_until_time_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_79 = None
        else:
            self.time_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_79 = None
        else:
            self.value_until_time_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_80 = None
        else:
            self.time_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_80 = None
        else:
            self.value_until_time_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_81 = None
        else:
            self.time_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_81 = None
        else:
            self.value_until_time_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_82 = None
        else:
            self.time_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_82 = None
        else:
            self.value_until_time_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_83 = None
        else:
            self.time_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_83 = None
        else:
            self.value_until_time_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_84 = None
        else:
            self.time_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_84 = None
        else:
            self.value_until_time_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_85 = None
        else:
            self.time_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_85 = None
        else:
            self.value_until_time_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_86 = None
        else:
            self.time_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_86 = None
        else:
            self.value_until_time_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_87 = None
        else:
            self.time_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_87 = None
        else:
            self.value_until_time_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_88 = None
        else:
            self.time_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_88 = None
        else:
            self.value_until_time_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_89 = None
        else:
            self.time_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_89 = None
        else:
            self.value_until_time_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_90 = None
        else:
            self.time_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_90 = None
        else:
            self.value_until_time_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_91 = None
        else:
            self.time_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_91 = None
        else:
            self.value_until_time_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_92 = None
        else:
            self.time_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_92 = None
        else:
            self.value_until_time_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_93 = None
        else:
            self.time_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_93 = None
        else:
            self.value_until_time_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_94 = None
        else:
            self.time_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_94 = None
        else:
            self.value_until_time_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_95 = None
        else:
            self.time_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_95 = None
        else:
            self.value_until_time_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_96 = None
        else:
            self.time_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_96 = None
        else:
            self.value_until_time_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_97 = None
        else:
            self.time_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_97 = None
        else:
            self.value_until_time_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_98 = None
        else:
            self.time_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_98 = None
        else:
            self.value_until_time_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_99 = None
        else:
            self.time_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_99 = None
        else:
            self.value_until_time_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_100 = None
        else:
            self.time_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_100 = None
        else:
            self.value_until_time_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_101 = None
        else:
            self.time_101 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_101 = None
        else:
            self.value_until_time_101 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_102 = None
        else:
            self.time_102 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_102 = None
        else:
            self.value_until_time_102 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_103 = None
        else:
            self.time_103 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_103 = None
        else:
            self.value_until_time_103 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_104 = None
        else:
            self.time_104 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_104 = None
        else:
            self.value_until_time_104 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_105 = None
        else:
            self.time_105 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_105 = None
        else:
            self.value_until_time_105 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_106 = None
        else:
            self.time_106 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_106 = None
        else:
            self.value_until_time_106 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_107 = None
        else:
            self.time_107 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_107 = None
        else:
            self.value_until_time_107 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_108 = None
        else:
            self.time_108 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_108 = None
        else:
            self.value_until_time_108 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_109 = None
        else:
            self.time_109 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_109 = None
        else:
            self.value_until_time_109 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_110 = None
        else:
            self.time_110 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_110 = None
        else:
            self.value_until_time_110 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_111 = None
        else:
            self.time_111 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_111 = None
        else:
            self.value_until_time_111 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_112 = None
        else:
            self.time_112 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_112 = None
        else:
            self.value_until_time_112 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_113 = None
        else:
            self.time_113 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_113 = None
        else:
            self.value_until_time_113 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_114 = None
        else:
            self.time_114 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_114 = None
        else:
            self.value_until_time_114 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_115 = None
        else:
            self.time_115 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_115 = None
        else:
            self.value_until_time_115 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_116 = None
        else:
            self.time_116 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_116 = None
        else:
            self.value_until_time_116 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_117 = None
        else:
            self.time_117 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_117 = None
        else:
            self.value_until_time_117 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_118 = None
        else:
            self.time_118 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_118 = None
        else:
            self.value_until_time_118 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_119 = None
        else:
            self.time_119 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_119 = None
        else:
            self.value_until_time_119 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_120 = None
        else:
            self.time_120 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_120 = None
        else:
            self.value_until_time_120 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_121 = None
        else:
            self.time_121 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_121 = None
        else:
            self.value_until_time_121 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_122 = None
        else:
            self.time_122 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_122 = None
        else:
            self.value_until_time_122 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_123 = None
        else:
            self.time_123 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_123 = None
        else:
            self.value_until_time_123 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_124 = None
        else:
            self.time_124 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_124 = None
        else:
            self.value_until_time_124 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_125 = None
        else:
            self.time_125 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_125 = None
        else:
            self.value_until_time_125 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_126 = None
        else:
            self.time_126 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_126 = None
        else:
            self.value_until_time_126 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_127 = None
        else:
            self.time_127 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_127 = None
        else:
            self.value_until_time_127 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_128 = None
        else:
            self.time_128 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_128 = None
        else:
            self.value_until_time_128 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_129 = None
        else:
            self.time_129 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_129 = None
        else:
            self.value_until_time_129 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_130 = None
        else:
            self.time_130 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_130 = None
        else:
            self.value_until_time_130 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_131 = None
        else:
            self.time_131 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_131 = None
        else:
            self.value_until_time_131 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_132 = None
        else:
            self.time_132 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_132 = None
        else:
            self.value_until_time_132 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_133 = None
        else:
            self.time_133 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_133 = None
        else:
            self.value_until_time_133 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_134 = None
        else:
            self.time_134 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_134 = None
        else:
            self.value_until_time_134 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_135 = None
        else:
            self.time_135 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_135 = None
        else:
            self.value_until_time_135 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_136 = None
        else:
            self.time_136 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_136 = None
        else:
            self.value_until_time_136 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_137 = None
        else:
            self.time_137 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_137 = None
        else:
            self.value_until_time_137 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_138 = None
        else:
            self.time_138 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_138 = None
        else:
            self.value_until_time_138 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_139 = None
        else:
            self.time_139 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_139 = None
        else:
            self.value_until_time_139 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_140 = None
        else:
            self.time_140 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_140 = None
        else:
            self.value_until_time_140 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_141 = None
        else:
            self.time_141 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_141 = None
        else:
            self.value_until_time_141 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_142 = None
        else:
            self.time_142 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_142 = None
        else:
            self.value_until_time_142 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_143 = None
        else:
            self.time_143 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_143 = None
        else:
            self.value_until_time_143 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_144 = None
        else:
            self.time_144 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_until_time_144 = None
        else:
            self.value_until_time_144 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_name`

        Args:
            value (str): value for IDD Field `schedule_type_limits_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_name`')

        self._data["Schedule Type Limits Name"] = value

    @property
    def interpolate_to_timestep(self):
        """Get interpolate_to_timestep

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set
        """
        return self._data["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """  Corresponds to IDD Field `interpolate_to_timestep`
        when the interval does not match the user specified timestep a Yes choice will average between the intervals request (to
        timestep resolution.  a No choice will use the interval value at the simulation timestep without regard to if it matches
        the boundary or not.

        Args:
            value (str): value for IDD Field `interpolate_to_timestep`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `interpolate_to_timestep`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `interpolate_to_timestep`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `interpolate_to_timestep`'.format(value))

        self._data["Interpolate to Timestep"] = value

    @property
    def time_1(self):
        """Get time_1

        Returns:
            str: the value of `time_1` or None if not set
        """
        return self._data["Time 1"]

    @time_1.setter
    def time_1(self, value=None):
        """  Corresponds to IDD Field `time_1`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_1`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_1`')

        self._data["Time 1"] = value

    @property
    def value_until_time_1(self):
        """Get value_until_time_1

        Returns:
            float: the value of `value_until_time_1` or None if not set
        """
        return self._data["Value Until Time 1"]

    @value_until_time_1.setter
    def value_until_time_1(self, value=None):
        """  Corresponds to IDD Field `value_until_time_1`

        Args:
            value (float): value for IDD Field `value_until_time_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_1`'.format(value))

        self._data["Value Until Time 1"] = value

    @property
    def time_2(self):
        """Get time_2

        Returns:
            str: the value of `time_2` or None if not set
        """
        return self._data["Time 2"]

    @time_2.setter
    def time_2(self, value=None):
        """  Corresponds to IDD Field `time_2`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_2`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_2`')

        self._data["Time 2"] = value

    @property
    def value_until_time_2(self):
        """Get value_until_time_2

        Returns:
            float: the value of `value_until_time_2` or None if not set
        """
        return self._data["Value Until Time 2"]

    @value_until_time_2.setter
    def value_until_time_2(self, value=None):
        """  Corresponds to IDD Field `value_until_time_2`

        Args:
            value (float): value for IDD Field `value_until_time_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_2`'.format(value))

        self._data["Value Until Time 2"] = value

    @property
    def time_3(self):
        """Get time_3

        Returns:
            str: the value of `time_3` or None if not set
        """
        return self._data["Time 3"]

    @time_3.setter
    def time_3(self, value=None):
        """  Corresponds to IDD Field `time_3`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_3`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_3`')

        self._data["Time 3"] = value

    @property
    def value_until_time_3(self):
        """Get value_until_time_3

        Returns:
            float: the value of `value_until_time_3` or None if not set
        """
        return self._data["Value Until Time 3"]

    @value_until_time_3.setter
    def value_until_time_3(self, value=None):
        """  Corresponds to IDD Field `value_until_time_3`

        Args:
            value (float): value for IDD Field `value_until_time_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_3`'.format(value))

        self._data["Value Until Time 3"] = value

    @property
    def time_4(self):
        """Get time_4

        Returns:
            str: the value of `time_4` or None if not set
        """
        return self._data["Time 4"]

    @time_4.setter
    def time_4(self, value=None):
        """  Corresponds to IDD Field `time_4`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_4`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_4`')

        self._data["Time 4"] = value

    @property
    def value_until_time_4(self):
        """Get value_until_time_4

        Returns:
            float: the value of `value_until_time_4` or None if not set
        """
        return self._data["Value Until Time 4"]

    @value_until_time_4.setter
    def value_until_time_4(self, value=None):
        """  Corresponds to IDD Field `value_until_time_4`

        Args:
            value (float): value for IDD Field `value_until_time_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_4`'.format(value))

        self._data["Value Until Time 4"] = value

    @property
    def time_5(self):
        """Get time_5

        Returns:
            str: the value of `time_5` or None if not set
        """
        return self._data["Time 5"]

    @time_5.setter
    def time_5(self, value=None):
        """  Corresponds to IDD Field `time_5`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_5`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_5`')

        self._data["Time 5"] = value

    @property
    def value_until_time_5(self):
        """Get value_until_time_5

        Returns:
            float: the value of `value_until_time_5` or None if not set
        """
        return self._data["Value Until Time 5"]

    @value_until_time_5.setter
    def value_until_time_5(self, value=None):
        """  Corresponds to IDD Field `value_until_time_5`

        Args:
            value (float): value for IDD Field `value_until_time_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_5`'.format(value))

        self._data["Value Until Time 5"] = value

    @property
    def time_6(self):
        """Get time_6

        Returns:
            str: the value of `time_6` or None if not set
        """
        return self._data["Time 6"]

    @time_6.setter
    def time_6(self, value=None):
        """  Corresponds to IDD Field `time_6`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_6`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_6`')

        self._data["Time 6"] = value

    @property
    def value_until_time_6(self):
        """Get value_until_time_6

        Returns:
            float: the value of `value_until_time_6` or None if not set
        """
        return self._data["Value Until Time 6"]

    @value_until_time_6.setter
    def value_until_time_6(self, value=None):
        """  Corresponds to IDD Field `value_until_time_6`

        Args:
            value (float): value for IDD Field `value_until_time_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_6`'.format(value))

        self._data["Value Until Time 6"] = value

    @property
    def time_7(self):
        """Get time_7

        Returns:
            str: the value of `time_7` or None if not set
        """
        return self._data["Time 7"]

    @time_7.setter
    def time_7(self, value=None):
        """  Corresponds to IDD Field `time_7`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_7`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_7`')

        self._data["Time 7"] = value

    @property
    def value_until_time_7(self):
        """Get value_until_time_7

        Returns:
            float: the value of `value_until_time_7` or None if not set
        """
        return self._data["Value Until Time 7"]

    @value_until_time_7.setter
    def value_until_time_7(self, value=None):
        """  Corresponds to IDD Field `value_until_time_7`

        Args:
            value (float): value for IDD Field `value_until_time_7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_7`'.format(value))

        self._data["Value Until Time 7"] = value

    @property
    def time_8(self):
        """Get time_8

        Returns:
            str: the value of `time_8` or None if not set
        """
        return self._data["Time 8"]

    @time_8.setter
    def time_8(self, value=None):
        """  Corresponds to IDD Field `time_8`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_8`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_8`')

        self._data["Time 8"] = value

    @property
    def value_until_time_8(self):
        """Get value_until_time_8

        Returns:
            float: the value of `value_until_time_8` or None if not set
        """
        return self._data["Value Until Time 8"]

    @value_until_time_8.setter
    def value_until_time_8(self, value=None):
        """  Corresponds to IDD Field `value_until_time_8`

        Args:
            value (float): value for IDD Field `value_until_time_8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_8`'.format(value))

        self._data["Value Until Time 8"] = value

    @property
    def time_9(self):
        """Get time_9

        Returns:
            str: the value of `time_9` or None if not set
        """
        return self._data["Time 9"]

    @time_9.setter
    def time_9(self, value=None):
        """  Corresponds to IDD Field `time_9`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_9`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_9`')

        self._data["Time 9"] = value

    @property
    def value_until_time_9(self):
        """Get value_until_time_9

        Returns:
            float: the value of `value_until_time_9` or None if not set
        """
        return self._data["Value Until Time 9"]

    @value_until_time_9.setter
    def value_until_time_9(self, value=None):
        """  Corresponds to IDD Field `value_until_time_9`

        Args:
            value (float): value for IDD Field `value_until_time_9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_9`'.format(value))

        self._data["Value Until Time 9"] = value

    @property
    def time_10(self):
        """Get time_10

        Returns:
            str: the value of `time_10` or None if not set
        """
        return self._data["Time 10"]

    @time_10.setter
    def time_10(self, value=None):
        """  Corresponds to IDD Field `time_10`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_10`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_10`')

        self._data["Time 10"] = value

    @property
    def value_until_time_10(self):
        """Get value_until_time_10

        Returns:
            float: the value of `value_until_time_10` or None if not set
        """
        return self._data["Value Until Time 10"]

    @value_until_time_10.setter
    def value_until_time_10(self, value=None):
        """  Corresponds to IDD Field `value_until_time_10`

        Args:
            value (float): value for IDD Field `value_until_time_10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_10`'.format(value))

        self._data["Value Until Time 10"] = value

    @property
    def time_11(self):
        """Get time_11

        Returns:
            str: the value of `time_11` or None if not set
        """
        return self._data["Time 11"]

    @time_11.setter
    def time_11(self, value=None):
        """  Corresponds to IDD Field `time_11`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_11`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_11`')

        self._data["Time 11"] = value

    @property
    def value_until_time_11(self):
        """Get value_until_time_11

        Returns:
            float: the value of `value_until_time_11` or None if not set
        """
        return self._data["Value Until Time 11"]

    @value_until_time_11.setter
    def value_until_time_11(self, value=None):
        """  Corresponds to IDD Field `value_until_time_11`

        Args:
            value (float): value for IDD Field `value_until_time_11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_11`'.format(value))

        self._data["Value Until Time 11"] = value

    @property
    def time_12(self):
        """Get time_12

        Returns:
            str: the value of `time_12` or None if not set
        """
        return self._data["Time 12"]

    @time_12.setter
    def time_12(self, value=None):
        """  Corresponds to IDD Field `time_12`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_12`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_12`')

        self._data["Time 12"] = value

    @property
    def value_until_time_12(self):
        """Get value_until_time_12

        Returns:
            float: the value of `value_until_time_12` or None if not set
        """
        return self._data["Value Until Time 12"]

    @value_until_time_12.setter
    def value_until_time_12(self, value=None):
        """  Corresponds to IDD Field `value_until_time_12`

        Args:
            value (float): value for IDD Field `value_until_time_12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_12`'.format(value))

        self._data["Value Until Time 12"] = value

    @property
    def time_13(self):
        """Get time_13

        Returns:
            str: the value of `time_13` or None if not set
        """
        return self._data["Time 13"]

    @time_13.setter
    def time_13(self, value=None):
        """  Corresponds to IDD Field `time_13`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_13`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_13`')

        self._data["Time 13"] = value

    @property
    def value_until_time_13(self):
        """Get value_until_time_13

        Returns:
            float: the value of `value_until_time_13` or None if not set
        """
        return self._data["Value Until Time 13"]

    @value_until_time_13.setter
    def value_until_time_13(self, value=None):
        """  Corresponds to IDD Field `value_until_time_13`

        Args:
            value (float): value for IDD Field `value_until_time_13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_13`'.format(value))

        self._data["Value Until Time 13"] = value

    @property
    def time_14(self):
        """Get time_14

        Returns:
            str: the value of `time_14` or None if not set
        """
        return self._data["Time 14"]

    @time_14.setter
    def time_14(self, value=None):
        """  Corresponds to IDD Field `time_14`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_14`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_14`')

        self._data["Time 14"] = value

    @property
    def value_until_time_14(self):
        """Get value_until_time_14

        Returns:
            float: the value of `value_until_time_14` or None if not set
        """
        return self._data["Value Until Time 14"]

    @value_until_time_14.setter
    def value_until_time_14(self, value=None):
        """  Corresponds to IDD Field `value_until_time_14`

        Args:
            value (float): value for IDD Field `value_until_time_14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_14`'.format(value))

        self._data["Value Until Time 14"] = value

    @property
    def time_15(self):
        """Get time_15

        Returns:
            str: the value of `time_15` or None if not set
        """
        return self._data["Time 15"]

    @time_15.setter
    def time_15(self, value=None):
        """  Corresponds to IDD Field `time_15`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_15`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_15`')

        self._data["Time 15"] = value

    @property
    def value_until_time_15(self):
        """Get value_until_time_15

        Returns:
            float: the value of `value_until_time_15` or None if not set
        """
        return self._data["Value Until Time 15"]

    @value_until_time_15.setter
    def value_until_time_15(self, value=None):
        """  Corresponds to IDD Field `value_until_time_15`

        Args:
            value (float): value for IDD Field `value_until_time_15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_15`'.format(value))

        self._data["Value Until Time 15"] = value

    @property
    def time_16(self):
        """Get time_16

        Returns:
            str: the value of `time_16` or None if not set
        """
        return self._data["Time 16"]

    @time_16.setter
    def time_16(self, value=None):
        """  Corresponds to IDD Field `time_16`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_16`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_16`')

        self._data["Time 16"] = value

    @property
    def value_until_time_16(self):
        """Get value_until_time_16

        Returns:
            float: the value of `value_until_time_16` or None if not set
        """
        return self._data["Value Until Time 16"]

    @value_until_time_16.setter
    def value_until_time_16(self, value=None):
        """  Corresponds to IDD Field `value_until_time_16`

        Args:
            value (float): value for IDD Field `value_until_time_16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_16`'.format(value))

        self._data["Value Until Time 16"] = value

    @property
    def time_17(self):
        """Get time_17

        Returns:
            str: the value of `time_17` or None if not set
        """
        return self._data["Time 17"]

    @time_17.setter
    def time_17(self, value=None):
        """  Corresponds to IDD Field `time_17`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_17`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_17`')

        self._data["Time 17"] = value

    @property
    def value_until_time_17(self):
        """Get value_until_time_17

        Returns:
            float: the value of `value_until_time_17` or None if not set
        """
        return self._data["Value Until Time 17"]

    @value_until_time_17.setter
    def value_until_time_17(self, value=None):
        """  Corresponds to IDD Field `value_until_time_17`

        Args:
            value (float): value for IDD Field `value_until_time_17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_17`'.format(value))

        self._data["Value Until Time 17"] = value

    @property
    def time_18(self):
        """Get time_18

        Returns:
            str: the value of `time_18` or None if not set
        """
        return self._data["Time 18"]

    @time_18.setter
    def time_18(self, value=None):
        """  Corresponds to IDD Field `time_18`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_18`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_18`')

        self._data["Time 18"] = value

    @property
    def value_until_time_18(self):
        """Get value_until_time_18

        Returns:
            float: the value of `value_until_time_18` or None if not set
        """
        return self._data["Value Until Time 18"]

    @value_until_time_18.setter
    def value_until_time_18(self, value=None):
        """  Corresponds to IDD Field `value_until_time_18`

        Args:
            value (float): value for IDD Field `value_until_time_18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_18`'.format(value))

        self._data["Value Until Time 18"] = value

    @property
    def time_19(self):
        """Get time_19

        Returns:
            str: the value of `time_19` or None if not set
        """
        return self._data["Time 19"]

    @time_19.setter
    def time_19(self, value=None):
        """  Corresponds to IDD Field `time_19`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_19`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_19`')

        self._data["Time 19"] = value

    @property
    def value_until_time_19(self):
        """Get value_until_time_19

        Returns:
            float: the value of `value_until_time_19` or None if not set
        """
        return self._data["Value Until Time 19"]

    @value_until_time_19.setter
    def value_until_time_19(self, value=None):
        """  Corresponds to IDD Field `value_until_time_19`

        Args:
            value (float): value for IDD Field `value_until_time_19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_19`'.format(value))

        self._data["Value Until Time 19"] = value

    @property
    def time_20(self):
        """Get time_20

        Returns:
            str: the value of `time_20` or None if not set
        """
        return self._data["Time 20"]

    @time_20.setter
    def time_20(self, value=None):
        """  Corresponds to IDD Field `time_20`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_20`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_20`')

        self._data["Time 20"] = value

    @property
    def value_until_time_20(self):
        """Get value_until_time_20

        Returns:
            float: the value of `value_until_time_20` or None if not set
        """
        return self._data["Value Until Time 20"]

    @value_until_time_20.setter
    def value_until_time_20(self, value=None):
        """  Corresponds to IDD Field `value_until_time_20`

        Args:
            value (float): value for IDD Field `value_until_time_20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_20`'.format(value))

        self._data["Value Until Time 20"] = value

    @property
    def time_21(self):
        """Get time_21

        Returns:
            str: the value of `time_21` or None if not set
        """
        return self._data["Time 21"]

    @time_21.setter
    def time_21(self, value=None):
        """  Corresponds to IDD Field `time_21`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_21`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_21`')

        self._data["Time 21"] = value

    @property
    def value_until_time_21(self):
        """Get value_until_time_21

        Returns:
            float: the value of `value_until_time_21` or None if not set
        """
        return self._data["Value Until Time 21"]

    @value_until_time_21.setter
    def value_until_time_21(self, value=None):
        """  Corresponds to IDD Field `value_until_time_21`

        Args:
            value (float): value for IDD Field `value_until_time_21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_21`'.format(value))

        self._data["Value Until Time 21"] = value

    @property
    def time_22(self):
        """Get time_22

        Returns:
            str: the value of `time_22` or None if not set
        """
        return self._data["Time 22"]

    @time_22.setter
    def time_22(self, value=None):
        """  Corresponds to IDD Field `time_22`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_22`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_22`')

        self._data["Time 22"] = value

    @property
    def value_until_time_22(self):
        """Get value_until_time_22

        Returns:
            float: the value of `value_until_time_22` or None if not set
        """
        return self._data["Value Until Time 22"]

    @value_until_time_22.setter
    def value_until_time_22(self, value=None):
        """  Corresponds to IDD Field `value_until_time_22`

        Args:
            value (float): value for IDD Field `value_until_time_22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_22`'.format(value))

        self._data["Value Until Time 22"] = value

    @property
    def time_23(self):
        """Get time_23

        Returns:
            str: the value of `time_23` or None if not set
        """
        return self._data["Time 23"]

    @time_23.setter
    def time_23(self, value=None):
        """  Corresponds to IDD Field `time_23`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_23`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_23`')

        self._data["Time 23"] = value

    @property
    def value_until_time_23(self):
        """Get value_until_time_23

        Returns:
            float: the value of `value_until_time_23` or None if not set
        """
        return self._data["Value Until Time 23"]

    @value_until_time_23.setter
    def value_until_time_23(self, value=None):
        """  Corresponds to IDD Field `value_until_time_23`

        Args:
            value (float): value for IDD Field `value_until_time_23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_23`'.format(value))

        self._data["Value Until Time 23"] = value

    @property
    def time_24(self):
        """Get time_24

        Returns:
            str: the value of `time_24` or None if not set
        """
        return self._data["Time 24"]

    @time_24.setter
    def time_24(self, value=None):
        """  Corresponds to IDD Field `time_24`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_24`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_24`')

        self._data["Time 24"] = value

    @property
    def value_until_time_24(self):
        """Get value_until_time_24

        Returns:
            float: the value of `value_until_time_24` or None if not set
        """
        return self._data["Value Until Time 24"]

    @value_until_time_24.setter
    def value_until_time_24(self, value=None):
        """  Corresponds to IDD Field `value_until_time_24`

        Args:
            value (float): value for IDD Field `value_until_time_24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_24`'.format(value))

        self._data["Value Until Time 24"] = value

    @property
    def time_25(self):
        """Get time_25

        Returns:
            str: the value of `time_25` or None if not set
        """
        return self._data["Time 25"]

    @time_25.setter
    def time_25(self, value=None):
        """  Corresponds to IDD Field `time_25`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_25`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_25`')

        self._data["Time 25"] = value

    @property
    def value_until_time_25(self):
        """Get value_until_time_25

        Returns:
            float: the value of `value_until_time_25` or None if not set
        """
        return self._data["Value Until Time 25"]

    @value_until_time_25.setter
    def value_until_time_25(self, value=None):
        """  Corresponds to IDD Field `value_until_time_25`

        Args:
            value (float): value for IDD Field `value_until_time_25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_25`'.format(value))

        self._data["Value Until Time 25"] = value

    @property
    def time_26(self):
        """Get time_26

        Returns:
            str: the value of `time_26` or None if not set
        """
        return self._data["Time 26"]

    @time_26.setter
    def time_26(self, value=None):
        """  Corresponds to IDD Field `time_26`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_26`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_26`')

        self._data["Time 26"] = value

    @property
    def value_until_time_26(self):
        """Get value_until_time_26

        Returns:
            float: the value of `value_until_time_26` or None if not set
        """
        return self._data["Value Until Time 26"]

    @value_until_time_26.setter
    def value_until_time_26(self, value=None):
        """  Corresponds to IDD Field `value_until_time_26`

        Args:
            value (float): value for IDD Field `value_until_time_26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_26`'.format(value))

        self._data["Value Until Time 26"] = value

    @property
    def time_27(self):
        """Get time_27

        Returns:
            str: the value of `time_27` or None if not set
        """
        return self._data["Time 27"]

    @time_27.setter
    def time_27(self, value=None):
        """  Corresponds to IDD Field `time_27`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_27`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_27`')

        self._data["Time 27"] = value

    @property
    def value_until_time_27(self):
        """Get value_until_time_27

        Returns:
            float: the value of `value_until_time_27` or None if not set
        """
        return self._data["Value Until Time 27"]

    @value_until_time_27.setter
    def value_until_time_27(self, value=None):
        """  Corresponds to IDD Field `value_until_time_27`

        Args:
            value (float): value for IDD Field `value_until_time_27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_27`'.format(value))

        self._data["Value Until Time 27"] = value

    @property
    def time_28(self):
        """Get time_28

        Returns:
            str: the value of `time_28` or None if not set
        """
        return self._data["Time 28"]

    @time_28.setter
    def time_28(self, value=None):
        """  Corresponds to IDD Field `time_28`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_28`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_28`')

        self._data["Time 28"] = value

    @property
    def value_until_time_28(self):
        """Get value_until_time_28

        Returns:
            float: the value of `value_until_time_28` or None if not set
        """
        return self._data["Value Until Time 28"]

    @value_until_time_28.setter
    def value_until_time_28(self, value=None):
        """  Corresponds to IDD Field `value_until_time_28`

        Args:
            value (float): value for IDD Field `value_until_time_28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_28`'.format(value))

        self._data["Value Until Time 28"] = value

    @property
    def time_29(self):
        """Get time_29

        Returns:
            str: the value of `time_29` or None if not set
        """
        return self._data["Time 29"]

    @time_29.setter
    def time_29(self, value=None):
        """  Corresponds to IDD Field `time_29`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_29`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_29`')

        self._data["Time 29"] = value

    @property
    def value_until_time_29(self):
        """Get value_until_time_29

        Returns:
            float: the value of `value_until_time_29` or None if not set
        """
        return self._data["Value Until Time 29"]

    @value_until_time_29.setter
    def value_until_time_29(self, value=None):
        """  Corresponds to IDD Field `value_until_time_29`

        Args:
            value (float): value for IDD Field `value_until_time_29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_29`'.format(value))

        self._data["Value Until Time 29"] = value

    @property
    def time_30(self):
        """Get time_30

        Returns:
            str: the value of `time_30` or None if not set
        """
        return self._data["Time 30"]

    @time_30.setter
    def time_30(self, value=None):
        """  Corresponds to IDD Field `time_30`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_30`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_30`')

        self._data["Time 30"] = value

    @property
    def value_until_time_30(self):
        """Get value_until_time_30

        Returns:
            float: the value of `value_until_time_30` or None if not set
        """
        return self._data["Value Until Time 30"]

    @value_until_time_30.setter
    def value_until_time_30(self, value=None):
        """  Corresponds to IDD Field `value_until_time_30`

        Args:
            value (float): value for IDD Field `value_until_time_30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_30`'.format(value))

        self._data["Value Until Time 30"] = value

    @property
    def time_31(self):
        """Get time_31

        Returns:
            str: the value of `time_31` or None if not set
        """
        return self._data["Time 31"]

    @time_31.setter
    def time_31(self, value=None):
        """  Corresponds to IDD Field `time_31`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_31`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_31`')

        self._data["Time 31"] = value

    @property
    def value_until_time_31(self):
        """Get value_until_time_31

        Returns:
            float: the value of `value_until_time_31` or None if not set
        """
        return self._data["Value Until Time 31"]

    @value_until_time_31.setter
    def value_until_time_31(self, value=None):
        """  Corresponds to IDD Field `value_until_time_31`

        Args:
            value (float): value for IDD Field `value_until_time_31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_31`'.format(value))

        self._data["Value Until Time 31"] = value

    @property
    def time_32(self):
        """Get time_32

        Returns:
            str: the value of `time_32` or None if not set
        """
        return self._data["Time 32"]

    @time_32.setter
    def time_32(self, value=None):
        """  Corresponds to IDD Field `time_32`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_32`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_32`')

        self._data["Time 32"] = value

    @property
    def value_until_time_32(self):
        """Get value_until_time_32

        Returns:
            float: the value of `value_until_time_32` or None if not set
        """
        return self._data["Value Until Time 32"]

    @value_until_time_32.setter
    def value_until_time_32(self, value=None):
        """  Corresponds to IDD Field `value_until_time_32`

        Args:
            value (float): value for IDD Field `value_until_time_32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_32`'.format(value))

        self._data["Value Until Time 32"] = value

    @property
    def time_33(self):
        """Get time_33

        Returns:
            str: the value of `time_33` or None if not set
        """
        return self._data["Time 33"]

    @time_33.setter
    def time_33(self, value=None):
        """  Corresponds to IDD Field `time_33`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_33`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_33`')

        self._data["Time 33"] = value

    @property
    def value_until_time_33(self):
        """Get value_until_time_33

        Returns:
            float: the value of `value_until_time_33` or None if not set
        """
        return self._data["Value Until Time 33"]

    @value_until_time_33.setter
    def value_until_time_33(self, value=None):
        """  Corresponds to IDD Field `value_until_time_33`

        Args:
            value (float): value for IDD Field `value_until_time_33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_33`'.format(value))

        self._data["Value Until Time 33"] = value

    @property
    def time_34(self):
        """Get time_34

        Returns:
            str: the value of `time_34` or None if not set
        """
        return self._data["Time 34"]

    @time_34.setter
    def time_34(self, value=None):
        """  Corresponds to IDD Field `time_34`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_34`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_34`')

        self._data["Time 34"] = value

    @property
    def value_until_time_34(self):
        """Get value_until_time_34

        Returns:
            float: the value of `value_until_time_34` or None if not set
        """
        return self._data["Value Until Time 34"]

    @value_until_time_34.setter
    def value_until_time_34(self, value=None):
        """  Corresponds to IDD Field `value_until_time_34`

        Args:
            value (float): value for IDD Field `value_until_time_34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_34`'.format(value))

        self._data["Value Until Time 34"] = value

    @property
    def time_35(self):
        """Get time_35

        Returns:
            str: the value of `time_35` or None if not set
        """
        return self._data["Time 35"]

    @time_35.setter
    def time_35(self, value=None):
        """  Corresponds to IDD Field `time_35`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_35`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_35`')

        self._data["Time 35"] = value

    @property
    def value_until_time_35(self):
        """Get value_until_time_35

        Returns:
            float: the value of `value_until_time_35` or None if not set
        """
        return self._data["Value Until Time 35"]

    @value_until_time_35.setter
    def value_until_time_35(self, value=None):
        """  Corresponds to IDD Field `value_until_time_35`

        Args:
            value (float): value for IDD Field `value_until_time_35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_35`'.format(value))

        self._data["Value Until Time 35"] = value

    @property
    def time_36(self):
        """Get time_36

        Returns:
            str: the value of `time_36` or None if not set
        """
        return self._data["Time 36"]

    @time_36.setter
    def time_36(self, value=None):
        """  Corresponds to IDD Field `time_36`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_36`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_36`')

        self._data["Time 36"] = value

    @property
    def value_until_time_36(self):
        """Get value_until_time_36

        Returns:
            float: the value of `value_until_time_36` or None if not set
        """
        return self._data["Value Until Time 36"]

    @value_until_time_36.setter
    def value_until_time_36(self, value=None):
        """  Corresponds to IDD Field `value_until_time_36`

        Args:
            value (float): value for IDD Field `value_until_time_36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_36`'.format(value))

        self._data["Value Until Time 36"] = value

    @property
    def time_37(self):
        """Get time_37

        Returns:
            str: the value of `time_37` or None if not set
        """
        return self._data["Time 37"]

    @time_37.setter
    def time_37(self, value=None):
        """  Corresponds to IDD Field `time_37`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_37`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_37`')

        self._data["Time 37"] = value

    @property
    def value_until_time_37(self):
        """Get value_until_time_37

        Returns:
            float: the value of `value_until_time_37` or None if not set
        """
        return self._data["Value Until Time 37"]

    @value_until_time_37.setter
    def value_until_time_37(self, value=None):
        """  Corresponds to IDD Field `value_until_time_37`

        Args:
            value (float): value for IDD Field `value_until_time_37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_37`'.format(value))

        self._data["Value Until Time 37"] = value

    @property
    def time_38(self):
        """Get time_38

        Returns:
            str: the value of `time_38` or None if not set
        """
        return self._data["Time 38"]

    @time_38.setter
    def time_38(self, value=None):
        """  Corresponds to IDD Field `time_38`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_38`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_38`')

        self._data["Time 38"] = value

    @property
    def value_until_time_38(self):
        """Get value_until_time_38

        Returns:
            float: the value of `value_until_time_38` or None if not set
        """
        return self._data["Value Until Time 38"]

    @value_until_time_38.setter
    def value_until_time_38(self, value=None):
        """  Corresponds to IDD Field `value_until_time_38`

        Args:
            value (float): value for IDD Field `value_until_time_38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_38`'.format(value))

        self._data["Value Until Time 38"] = value

    @property
    def time_39(self):
        """Get time_39

        Returns:
            str: the value of `time_39` or None if not set
        """
        return self._data["Time 39"]

    @time_39.setter
    def time_39(self, value=None):
        """  Corresponds to IDD Field `time_39`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_39`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_39`')

        self._data["Time 39"] = value

    @property
    def value_until_time_39(self):
        """Get value_until_time_39

        Returns:
            float: the value of `value_until_time_39` or None if not set
        """
        return self._data["Value Until Time 39"]

    @value_until_time_39.setter
    def value_until_time_39(self, value=None):
        """  Corresponds to IDD Field `value_until_time_39`

        Args:
            value (float): value for IDD Field `value_until_time_39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_39`'.format(value))

        self._data["Value Until Time 39"] = value

    @property
    def time_40(self):
        """Get time_40

        Returns:
            str: the value of `time_40` or None if not set
        """
        return self._data["Time 40"]

    @time_40.setter
    def time_40(self, value=None):
        """  Corresponds to IDD Field `time_40`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_40`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_40`')

        self._data["Time 40"] = value

    @property
    def value_until_time_40(self):
        """Get value_until_time_40

        Returns:
            float: the value of `value_until_time_40` or None if not set
        """
        return self._data["Value Until Time 40"]

    @value_until_time_40.setter
    def value_until_time_40(self, value=None):
        """  Corresponds to IDD Field `value_until_time_40`

        Args:
            value (float): value for IDD Field `value_until_time_40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_40`'.format(value))

        self._data["Value Until Time 40"] = value

    @property
    def time_41(self):
        """Get time_41

        Returns:
            str: the value of `time_41` or None if not set
        """
        return self._data["Time 41"]

    @time_41.setter
    def time_41(self, value=None):
        """  Corresponds to IDD Field `time_41`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_41`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_41`')

        self._data["Time 41"] = value

    @property
    def value_until_time_41(self):
        """Get value_until_time_41

        Returns:
            float: the value of `value_until_time_41` or None if not set
        """
        return self._data["Value Until Time 41"]

    @value_until_time_41.setter
    def value_until_time_41(self, value=None):
        """  Corresponds to IDD Field `value_until_time_41`

        Args:
            value (float): value for IDD Field `value_until_time_41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_41`'.format(value))

        self._data["Value Until Time 41"] = value

    @property
    def time_42(self):
        """Get time_42

        Returns:
            str: the value of `time_42` or None if not set
        """
        return self._data["Time 42"]

    @time_42.setter
    def time_42(self, value=None):
        """  Corresponds to IDD Field `time_42`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_42`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_42`')

        self._data["Time 42"] = value

    @property
    def value_until_time_42(self):
        """Get value_until_time_42

        Returns:
            float: the value of `value_until_time_42` or None if not set
        """
        return self._data["Value Until Time 42"]

    @value_until_time_42.setter
    def value_until_time_42(self, value=None):
        """  Corresponds to IDD Field `value_until_time_42`

        Args:
            value (float): value for IDD Field `value_until_time_42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_42`'.format(value))

        self._data["Value Until Time 42"] = value

    @property
    def time_43(self):
        """Get time_43

        Returns:
            str: the value of `time_43` or None if not set
        """
        return self._data["Time 43"]

    @time_43.setter
    def time_43(self, value=None):
        """  Corresponds to IDD Field `time_43`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_43`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_43`')

        self._data["Time 43"] = value

    @property
    def value_until_time_43(self):
        """Get value_until_time_43

        Returns:
            float: the value of `value_until_time_43` or None if not set
        """
        return self._data["Value Until Time 43"]

    @value_until_time_43.setter
    def value_until_time_43(self, value=None):
        """  Corresponds to IDD Field `value_until_time_43`

        Args:
            value (float): value for IDD Field `value_until_time_43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_43`'.format(value))

        self._data["Value Until Time 43"] = value

    @property
    def time_44(self):
        """Get time_44

        Returns:
            str: the value of `time_44` or None if not set
        """
        return self._data["Time 44"]

    @time_44.setter
    def time_44(self, value=None):
        """  Corresponds to IDD Field `time_44`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_44`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_44`')

        self._data["Time 44"] = value

    @property
    def value_until_time_44(self):
        """Get value_until_time_44

        Returns:
            float: the value of `value_until_time_44` or None if not set
        """
        return self._data["Value Until Time 44"]

    @value_until_time_44.setter
    def value_until_time_44(self, value=None):
        """  Corresponds to IDD Field `value_until_time_44`

        Args:
            value (float): value for IDD Field `value_until_time_44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_44`'.format(value))

        self._data["Value Until Time 44"] = value

    @property
    def time_45(self):
        """Get time_45

        Returns:
            str: the value of `time_45` or None if not set
        """
        return self._data["Time 45"]

    @time_45.setter
    def time_45(self, value=None):
        """  Corresponds to IDD Field `time_45`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_45`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_45`')

        self._data["Time 45"] = value

    @property
    def value_until_time_45(self):
        """Get value_until_time_45

        Returns:
            float: the value of `value_until_time_45` or None if not set
        """
        return self._data["Value Until Time 45"]

    @value_until_time_45.setter
    def value_until_time_45(self, value=None):
        """  Corresponds to IDD Field `value_until_time_45`

        Args:
            value (float): value for IDD Field `value_until_time_45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_45`'.format(value))

        self._data["Value Until Time 45"] = value

    @property
    def time_46(self):
        """Get time_46

        Returns:
            str: the value of `time_46` or None if not set
        """
        return self._data["Time 46"]

    @time_46.setter
    def time_46(self, value=None):
        """  Corresponds to IDD Field `time_46`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_46`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_46`')

        self._data["Time 46"] = value

    @property
    def value_until_time_46(self):
        """Get value_until_time_46

        Returns:
            float: the value of `value_until_time_46` or None if not set
        """
        return self._data["Value Until Time 46"]

    @value_until_time_46.setter
    def value_until_time_46(self, value=None):
        """  Corresponds to IDD Field `value_until_time_46`

        Args:
            value (float): value for IDD Field `value_until_time_46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_46`'.format(value))

        self._data["Value Until Time 46"] = value

    @property
    def time_47(self):
        """Get time_47

        Returns:
            str: the value of `time_47` or None if not set
        """
        return self._data["Time 47"]

    @time_47.setter
    def time_47(self, value=None):
        """  Corresponds to IDD Field `time_47`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_47`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_47`')

        self._data["Time 47"] = value

    @property
    def value_until_time_47(self):
        """Get value_until_time_47

        Returns:
            float: the value of `value_until_time_47` or None if not set
        """
        return self._data["Value Until Time 47"]

    @value_until_time_47.setter
    def value_until_time_47(self, value=None):
        """  Corresponds to IDD Field `value_until_time_47`

        Args:
            value (float): value for IDD Field `value_until_time_47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_47`'.format(value))

        self._data["Value Until Time 47"] = value

    @property
    def time_48(self):
        """Get time_48

        Returns:
            str: the value of `time_48` or None if not set
        """
        return self._data["Time 48"]

    @time_48.setter
    def time_48(self, value=None):
        """  Corresponds to IDD Field `time_48`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_48`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_48`')

        self._data["Time 48"] = value

    @property
    def value_until_time_48(self):
        """Get value_until_time_48

        Returns:
            float: the value of `value_until_time_48` or None if not set
        """
        return self._data["Value Until Time 48"]

    @value_until_time_48.setter
    def value_until_time_48(self, value=None):
        """  Corresponds to IDD Field `value_until_time_48`

        Args:
            value (float): value for IDD Field `value_until_time_48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_48`'.format(value))

        self._data["Value Until Time 48"] = value

    @property
    def time_49(self):
        """Get time_49

        Returns:
            str: the value of `time_49` or None if not set
        """
        return self._data["Time 49"]

    @time_49.setter
    def time_49(self, value=None):
        """  Corresponds to IDD Field `time_49`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_49`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_49`')

        self._data["Time 49"] = value

    @property
    def value_until_time_49(self):
        """Get value_until_time_49

        Returns:
            float: the value of `value_until_time_49` or None if not set
        """
        return self._data["Value Until Time 49"]

    @value_until_time_49.setter
    def value_until_time_49(self, value=None):
        """  Corresponds to IDD Field `value_until_time_49`

        Args:
            value (float): value for IDD Field `value_until_time_49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_49`'.format(value))

        self._data["Value Until Time 49"] = value

    @property
    def time_50(self):
        """Get time_50

        Returns:
            str: the value of `time_50` or None if not set
        """
        return self._data["Time 50"]

    @time_50.setter
    def time_50(self, value=None):
        """  Corresponds to IDD Field `time_50`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_50`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_50`')

        self._data["Time 50"] = value

    @property
    def value_until_time_50(self):
        """Get value_until_time_50

        Returns:
            float: the value of `value_until_time_50` or None if not set
        """
        return self._data["Value Until Time 50"]

    @value_until_time_50.setter
    def value_until_time_50(self, value=None):
        """  Corresponds to IDD Field `value_until_time_50`

        Args:
            value (float): value for IDD Field `value_until_time_50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_50`'.format(value))

        self._data["Value Until Time 50"] = value

    @property
    def time_51(self):
        """Get time_51

        Returns:
            str: the value of `time_51` or None if not set
        """
        return self._data["Time 51"]

    @time_51.setter
    def time_51(self, value=None):
        """  Corresponds to IDD Field `time_51`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_51`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_51`')

        self._data["Time 51"] = value

    @property
    def value_until_time_51(self):
        """Get value_until_time_51

        Returns:
            float: the value of `value_until_time_51` or None if not set
        """
        return self._data["Value Until Time 51"]

    @value_until_time_51.setter
    def value_until_time_51(self, value=None):
        """  Corresponds to IDD Field `value_until_time_51`

        Args:
            value (float): value for IDD Field `value_until_time_51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_51`'.format(value))

        self._data["Value Until Time 51"] = value

    @property
    def time_52(self):
        """Get time_52

        Returns:
            str: the value of `time_52` or None if not set
        """
        return self._data["Time 52"]

    @time_52.setter
    def time_52(self, value=None):
        """  Corresponds to IDD Field `time_52`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_52`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_52`')

        self._data["Time 52"] = value

    @property
    def value_until_time_52(self):
        """Get value_until_time_52

        Returns:
            float: the value of `value_until_time_52` or None if not set
        """
        return self._data["Value Until Time 52"]

    @value_until_time_52.setter
    def value_until_time_52(self, value=None):
        """  Corresponds to IDD Field `value_until_time_52`

        Args:
            value (float): value for IDD Field `value_until_time_52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_52`'.format(value))

        self._data["Value Until Time 52"] = value

    @property
    def time_53(self):
        """Get time_53

        Returns:
            str: the value of `time_53` or None if not set
        """
        return self._data["Time 53"]

    @time_53.setter
    def time_53(self, value=None):
        """  Corresponds to IDD Field `time_53`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_53`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_53`')

        self._data["Time 53"] = value

    @property
    def value_until_time_53(self):
        """Get value_until_time_53

        Returns:
            float: the value of `value_until_time_53` or None if not set
        """
        return self._data["Value Until Time 53"]

    @value_until_time_53.setter
    def value_until_time_53(self, value=None):
        """  Corresponds to IDD Field `value_until_time_53`

        Args:
            value (float): value for IDD Field `value_until_time_53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_53`'.format(value))

        self._data["Value Until Time 53"] = value

    @property
    def time_54(self):
        """Get time_54

        Returns:
            str: the value of `time_54` or None if not set
        """
        return self._data["Time 54"]

    @time_54.setter
    def time_54(self, value=None):
        """  Corresponds to IDD Field `time_54`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_54`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_54`')

        self._data["Time 54"] = value

    @property
    def value_until_time_54(self):
        """Get value_until_time_54

        Returns:
            float: the value of `value_until_time_54` or None if not set
        """
        return self._data["Value Until Time 54"]

    @value_until_time_54.setter
    def value_until_time_54(self, value=None):
        """  Corresponds to IDD Field `value_until_time_54`

        Args:
            value (float): value for IDD Field `value_until_time_54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_54`'.format(value))

        self._data["Value Until Time 54"] = value

    @property
    def time_55(self):
        """Get time_55

        Returns:
            str: the value of `time_55` or None if not set
        """
        return self._data["Time 55"]

    @time_55.setter
    def time_55(self, value=None):
        """  Corresponds to IDD Field `time_55`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_55`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_55`')

        self._data["Time 55"] = value

    @property
    def value_until_time_55(self):
        """Get value_until_time_55

        Returns:
            float: the value of `value_until_time_55` or None if not set
        """
        return self._data["Value Until Time 55"]

    @value_until_time_55.setter
    def value_until_time_55(self, value=None):
        """  Corresponds to IDD Field `value_until_time_55`

        Args:
            value (float): value for IDD Field `value_until_time_55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_55`'.format(value))

        self._data["Value Until Time 55"] = value

    @property
    def time_56(self):
        """Get time_56

        Returns:
            str: the value of `time_56` or None if not set
        """
        return self._data["Time 56"]

    @time_56.setter
    def time_56(self, value=None):
        """  Corresponds to IDD Field `time_56`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_56`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_56`')

        self._data["Time 56"] = value

    @property
    def value_until_time_56(self):
        """Get value_until_time_56

        Returns:
            float: the value of `value_until_time_56` or None if not set
        """
        return self._data["Value Until Time 56"]

    @value_until_time_56.setter
    def value_until_time_56(self, value=None):
        """  Corresponds to IDD Field `value_until_time_56`

        Args:
            value (float): value for IDD Field `value_until_time_56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_56`'.format(value))

        self._data["Value Until Time 56"] = value

    @property
    def time_57(self):
        """Get time_57

        Returns:
            str: the value of `time_57` or None if not set
        """
        return self._data["Time 57"]

    @time_57.setter
    def time_57(self, value=None):
        """  Corresponds to IDD Field `time_57`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_57`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_57`')

        self._data["Time 57"] = value

    @property
    def value_until_time_57(self):
        """Get value_until_time_57

        Returns:
            float: the value of `value_until_time_57` or None if not set
        """
        return self._data["Value Until Time 57"]

    @value_until_time_57.setter
    def value_until_time_57(self, value=None):
        """  Corresponds to IDD Field `value_until_time_57`

        Args:
            value (float): value for IDD Field `value_until_time_57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_57`'.format(value))

        self._data["Value Until Time 57"] = value

    @property
    def time_58(self):
        """Get time_58

        Returns:
            str: the value of `time_58` or None if not set
        """
        return self._data["Time 58"]

    @time_58.setter
    def time_58(self, value=None):
        """  Corresponds to IDD Field `time_58`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_58`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_58`')

        self._data["Time 58"] = value

    @property
    def value_until_time_58(self):
        """Get value_until_time_58

        Returns:
            float: the value of `value_until_time_58` or None if not set
        """
        return self._data["Value Until Time 58"]

    @value_until_time_58.setter
    def value_until_time_58(self, value=None):
        """  Corresponds to IDD Field `value_until_time_58`

        Args:
            value (float): value for IDD Field `value_until_time_58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_58`'.format(value))

        self._data["Value Until Time 58"] = value

    @property
    def time_59(self):
        """Get time_59

        Returns:
            str: the value of `time_59` or None if not set
        """
        return self._data["Time 59"]

    @time_59.setter
    def time_59(self, value=None):
        """  Corresponds to IDD Field `time_59`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_59`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_59`')

        self._data["Time 59"] = value

    @property
    def value_until_time_59(self):
        """Get value_until_time_59

        Returns:
            float: the value of `value_until_time_59` or None if not set
        """
        return self._data["Value Until Time 59"]

    @value_until_time_59.setter
    def value_until_time_59(self, value=None):
        """  Corresponds to IDD Field `value_until_time_59`

        Args:
            value (float): value for IDD Field `value_until_time_59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_59`'.format(value))

        self._data["Value Until Time 59"] = value

    @property
    def time_60(self):
        """Get time_60

        Returns:
            str: the value of `time_60` or None if not set
        """
        return self._data["Time 60"]

    @time_60.setter
    def time_60(self, value=None):
        """  Corresponds to IDD Field `time_60`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_60`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_60`')

        self._data["Time 60"] = value

    @property
    def value_until_time_60(self):
        """Get value_until_time_60

        Returns:
            float: the value of `value_until_time_60` or None if not set
        """
        return self._data["Value Until Time 60"]

    @value_until_time_60.setter
    def value_until_time_60(self, value=None):
        """  Corresponds to IDD Field `value_until_time_60`

        Args:
            value (float): value for IDD Field `value_until_time_60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_60`'.format(value))

        self._data["Value Until Time 60"] = value

    @property
    def time_61(self):
        """Get time_61

        Returns:
            str: the value of `time_61` or None if not set
        """
        return self._data["Time 61"]

    @time_61.setter
    def time_61(self, value=None):
        """  Corresponds to IDD Field `time_61`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_61`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_61`')

        self._data["Time 61"] = value

    @property
    def value_until_time_61(self):
        """Get value_until_time_61

        Returns:
            float: the value of `value_until_time_61` or None if not set
        """
        return self._data["Value Until Time 61"]

    @value_until_time_61.setter
    def value_until_time_61(self, value=None):
        """  Corresponds to IDD Field `value_until_time_61`

        Args:
            value (float): value for IDD Field `value_until_time_61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_61`'.format(value))

        self._data["Value Until Time 61"] = value

    @property
    def time_62(self):
        """Get time_62

        Returns:
            str: the value of `time_62` or None if not set
        """
        return self._data["Time 62"]

    @time_62.setter
    def time_62(self, value=None):
        """  Corresponds to IDD Field `time_62`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_62`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_62`')

        self._data["Time 62"] = value

    @property
    def value_until_time_62(self):
        """Get value_until_time_62

        Returns:
            float: the value of `value_until_time_62` or None if not set
        """
        return self._data["Value Until Time 62"]

    @value_until_time_62.setter
    def value_until_time_62(self, value=None):
        """  Corresponds to IDD Field `value_until_time_62`

        Args:
            value (float): value for IDD Field `value_until_time_62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_62`'.format(value))

        self._data["Value Until Time 62"] = value

    @property
    def time_63(self):
        """Get time_63

        Returns:
            str: the value of `time_63` or None if not set
        """
        return self._data["Time 63"]

    @time_63.setter
    def time_63(self, value=None):
        """  Corresponds to IDD Field `time_63`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_63`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_63`')

        self._data["Time 63"] = value

    @property
    def value_until_time_63(self):
        """Get value_until_time_63

        Returns:
            float: the value of `value_until_time_63` or None if not set
        """
        return self._data["Value Until Time 63"]

    @value_until_time_63.setter
    def value_until_time_63(self, value=None):
        """  Corresponds to IDD Field `value_until_time_63`

        Args:
            value (float): value for IDD Field `value_until_time_63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_63`'.format(value))

        self._data["Value Until Time 63"] = value

    @property
    def time_64(self):
        """Get time_64

        Returns:
            str: the value of `time_64` or None if not set
        """
        return self._data["Time 64"]

    @time_64.setter
    def time_64(self, value=None):
        """  Corresponds to IDD Field `time_64`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_64`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_64`')

        self._data["Time 64"] = value

    @property
    def value_until_time_64(self):
        """Get value_until_time_64

        Returns:
            float: the value of `value_until_time_64` or None if not set
        """
        return self._data["Value Until Time 64"]

    @value_until_time_64.setter
    def value_until_time_64(self, value=None):
        """  Corresponds to IDD Field `value_until_time_64`

        Args:
            value (float): value for IDD Field `value_until_time_64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_64`'.format(value))

        self._data["Value Until Time 64"] = value

    @property
    def time_65(self):
        """Get time_65

        Returns:
            str: the value of `time_65` or None if not set
        """
        return self._data["Time 65"]

    @time_65.setter
    def time_65(self, value=None):
        """  Corresponds to IDD Field `time_65`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_65`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_65`')

        self._data["Time 65"] = value

    @property
    def value_until_time_65(self):
        """Get value_until_time_65

        Returns:
            float: the value of `value_until_time_65` or None if not set
        """
        return self._data["Value Until Time 65"]

    @value_until_time_65.setter
    def value_until_time_65(self, value=None):
        """  Corresponds to IDD Field `value_until_time_65`

        Args:
            value (float): value for IDD Field `value_until_time_65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_65`'.format(value))

        self._data["Value Until Time 65"] = value

    @property
    def time_66(self):
        """Get time_66

        Returns:
            str: the value of `time_66` or None if not set
        """
        return self._data["Time 66"]

    @time_66.setter
    def time_66(self, value=None):
        """  Corresponds to IDD Field `time_66`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_66`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_66`')

        self._data["Time 66"] = value

    @property
    def value_until_time_66(self):
        """Get value_until_time_66

        Returns:
            float: the value of `value_until_time_66` or None if not set
        """
        return self._data["Value Until Time 66"]

    @value_until_time_66.setter
    def value_until_time_66(self, value=None):
        """  Corresponds to IDD Field `value_until_time_66`

        Args:
            value (float): value for IDD Field `value_until_time_66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_66`'.format(value))

        self._data["Value Until Time 66"] = value

    @property
    def time_67(self):
        """Get time_67

        Returns:
            str: the value of `time_67` or None if not set
        """
        return self._data["Time 67"]

    @time_67.setter
    def time_67(self, value=None):
        """  Corresponds to IDD Field `time_67`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_67`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_67`')

        self._data["Time 67"] = value

    @property
    def value_until_time_67(self):
        """Get value_until_time_67

        Returns:
            float: the value of `value_until_time_67` or None if not set
        """
        return self._data["Value Until Time 67"]

    @value_until_time_67.setter
    def value_until_time_67(self, value=None):
        """  Corresponds to IDD Field `value_until_time_67`

        Args:
            value (float): value for IDD Field `value_until_time_67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_67`'.format(value))

        self._data["Value Until Time 67"] = value

    @property
    def time_68(self):
        """Get time_68

        Returns:
            str: the value of `time_68` or None if not set
        """
        return self._data["Time 68"]

    @time_68.setter
    def time_68(self, value=None):
        """  Corresponds to IDD Field `time_68`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_68`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_68`')

        self._data["Time 68"] = value

    @property
    def value_until_time_68(self):
        """Get value_until_time_68

        Returns:
            float: the value of `value_until_time_68` or None if not set
        """
        return self._data["Value Until Time 68"]

    @value_until_time_68.setter
    def value_until_time_68(self, value=None):
        """  Corresponds to IDD Field `value_until_time_68`

        Args:
            value (float): value for IDD Field `value_until_time_68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_68`'.format(value))

        self._data["Value Until Time 68"] = value

    @property
    def time_69(self):
        """Get time_69

        Returns:
            str: the value of `time_69` or None if not set
        """
        return self._data["Time 69"]

    @time_69.setter
    def time_69(self, value=None):
        """  Corresponds to IDD Field `time_69`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_69`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_69`')

        self._data["Time 69"] = value

    @property
    def value_until_time_69(self):
        """Get value_until_time_69

        Returns:
            float: the value of `value_until_time_69` or None if not set
        """
        return self._data["Value Until Time 69"]

    @value_until_time_69.setter
    def value_until_time_69(self, value=None):
        """  Corresponds to IDD Field `value_until_time_69`

        Args:
            value (float): value for IDD Field `value_until_time_69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_69`'.format(value))

        self._data["Value Until Time 69"] = value

    @property
    def time_70(self):
        """Get time_70

        Returns:
            str: the value of `time_70` or None if not set
        """
        return self._data["Time 70"]

    @time_70.setter
    def time_70(self, value=None):
        """  Corresponds to IDD Field `time_70`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_70`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_70`')

        self._data["Time 70"] = value

    @property
    def value_until_time_70(self):
        """Get value_until_time_70

        Returns:
            float: the value of `value_until_time_70` or None if not set
        """
        return self._data["Value Until Time 70"]

    @value_until_time_70.setter
    def value_until_time_70(self, value=None):
        """  Corresponds to IDD Field `value_until_time_70`

        Args:
            value (float): value for IDD Field `value_until_time_70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_70`'.format(value))

        self._data["Value Until Time 70"] = value

    @property
    def time_71(self):
        """Get time_71

        Returns:
            str: the value of `time_71` or None if not set
        """
        return self._data["Time 71"]

    @time_71.setter
    def time_71(self, value=None):
        """  Corresponds to IDD Field `time_71`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_71`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_71`')

        self._data["Time 71"] = value

    @property
    def value_until_time_71(self):
        """Get value_until_time_71

        Returns:
            float: the value of `value_until_time_71` or None if not set
        """
        return self._data["Value Until Time 71"]

    @value_until_time_71.setter
    def value_until_time_71(self, value=None):
        """  Corresponds to IDD Field `value_until_time_71`

        Args:
            value (float): value for IDD Field `value_until_time_71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_71`'.format(value))

        self._data["Value Until Time 71"] = value

    @property
    def time_72(self):
        """Get time_72

        Returns:
            str: the value of `time_72` or None if not set
        """
        return self._data["Time 72"]

    @time_72.setter
    def time_72(self, value=None):
        """  Corresponds to IDD Field `time_72`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_72`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_72`')

        self._data["Time 72"] = value

    @property
    def value_until_time_72(self):
        """Get value_until_time_72

        Returns:
            float: the value of `value_until_time_72` or None if not set
        """
        return self._data["Value Until Time 72"]

    @value_until_time_72.setter
    def value_until_time_72(self, value=None):
        """  Corresponds to IDD Field `value_until_time_72`

        Args:
            value (float): value for IDD Field `value_until_time_72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_72`'.format(value))

        self._data["Value Until Time 72"] = value

    @property
    def time_73(self):
        """Get time_73

        Returns:
            str: the value of `time_73` or None if not set
        """
        return self._data["Time 73"]

    @time_73.setter
    def time_73(self, value=None):
        """  Corresponds to IDD Field `time_73`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_73`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_73`')

        self._data["Time 73"] = value

    @property
    def value_until_time_73(self):
        """Get value_until_time_73

        Returns:
            float: the value of `value_until_time_73` or None if not set
        """
        return self._data["Value Until Time 73"]

    @value_until_time_73.setter
    def value_until_time_73(self, value=None):
        """  Corresponds to IDD Field `value_until_time_73`

        Args:
            value (float): value for IDD Field `value_until_time_73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_73`'.format(value))

        self._data["Value Until Time 73"] = value

    @property
    def time_74(self):
        """Get time_74

        Returns:
            str: the value of `time_74` or None if not set
        """
        return self._data["Time 74"]

    @time_74.setter
    def time_74(self, value=None):
        """  Corresponds to IDD Field `time_74`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_74`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_74`')

        self._data["Time 74"] = value

    @property
    def value_until_time_74(self):
        """Get value_until_time_74

        Returns:
            float: the value of `value_until_time_74` or None if not set
        """
        return self._data["Value Until Time 74"]

    @value_until_time_74.setter
    def value_until_time_74(self, value=None):
        """  Corresponds to IDD Field `value_until_time_74`

        Args:
            value (float): value for IDD Field `value_until_time_74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_74`'.format(value))

        self._data["Value Until Time 74"] = value

    @property
    def time_75(self):
        """Get time_75

        Returns:
            str: the value of `time_75` or None if not set
        """
        return self._data["Time 75"]

    @time_75.setter
    def time_75(self, value=None):
        """  Corresponds to IDD Field `time_75`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_75`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_75`')

        self._data["Time 75"] = value

    @property
    def value_until_time_75(self):
        """Get value_until_time_75

        Returns:
            float: the value of `value_until_time_75` or None if not set
        """
        return self._data["Value Until Time 75"]

    @value_until_time_75.setter
    def value_until_time_75(self, value=None):
        """  Corresponds to IDD Field `value_until_time_75`

        Args:
            value (float): value for IDD Field `value_until_time_75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_75`'.format(value))

        self._data["Value Until Time 75"] = value

    @property
    def time_76(self):
        """Get time_76

        Returns:
            str: the value of `time_76` or None if not set
        """
        return self._data["Time 76"]

    @time_76.setter
    def time_76(self, value=None):
        """  Corresponds to IDD Field `time_76`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_76`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_76`')

        self._data["Time 76"] = value

    @property
    def value_until_time_76(self):
        """Get value_until_time_76

        Returns:
            float: the value of `value_until_time_76` or None if not set
        """
        return self._data["Value Until Time 76"]

    @value_until_time_76.setter
    def value_until_time_76(self, value=None):
        """  Corresponds to IDD Field `value_until_time_76`

        Args:
            value (float): value for IDD Field `value_until_time_76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_76`'.format(value))

        self._data["Value Until Time 76"] = value

    @property
    def time_77(self):
        """Get time_77

        Returns:
            str: the value of `time_77` or None if not set
        """
        return self._data["Time 77"]

    @time_77.setter
    def time_77(self, value=None):
        """  Corresponds to IDD Field `time_77`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_77`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_77`')

        self._data["Time 77"] = value

    @property
    def value_until_time_77(self):
        """Get value_until_time_77

        Returns:
            float: the value of `value_until_time_77` or None if not set
        """
        return self._data["Value Until Time 77"]

    @value_until_time_77.setter
    def value_until_time_77(self, value=None):
        """  Corresponds to IDD Field `value_until_time_77`

        Args:
            value (float): value for IDD Field `value_until_time_77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_77`'.format(value))

        self._data["Value Until Time 77"] = value

    @property
    def time_78(self):
        """Get time_78

        Returns:
            str: the value of `time_78` or None if not set
        """
        return self._data["Time 78"]

    @time_78.setter
    def time_78(self, value=None):
        """  Corresponds to IDD Field `time_78`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_78`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_78`')

        self._data["Time 78"] = value

    @property
    def value_until_time_78(self):
        """Get value_until_time_78

        Returns:
            float: the value of `value_until_time_78` or None if not set
        """
        return self._data["Value Until Time 78"]

    @value_until_time_78.setter
    def value_until_time_78(self, value=None):
        """  Corresponds to IDD Field `value_until_time_78`

        Args:
            value (float): value for IDD Field `value_until_time_78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_78`'.format(value))

        self._data["Value Until Time 78"] = value

    @property
    def time_79(self):
        """Get time_79

        Returns:
            str: the value of `time_79` or None if not set
        """
        return self._data["Time 79"]

    @time_79.setter
    def time_79(self, value=None):
        """  Corresponds to IDD Field `time_79`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_79`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_79`')

        self._data["Time 79"] = value

    @property
    def value_until_time_79(self):
        """Get value_until_time_79

        Returns:
            float: the value of `value_until_time_79` or None if not set
        """
        return self._data["Value Until Time 79"]

    @value_until_time_79.setter
    def value_until_time_79(self, value=None):
        """  Corresponds to IDD Field `value_until_time_79`

        Args:
            value (float): value for IDD Field `value_until_time_79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_79`'.format(value))

        self._data["Value Until Time 79"] = value

    @property
    def time_80(self):
        """Get time_80

        Returns:
            str: the value of `time_80` or None if not set
        """
        return self._data["Time 80"]

    @time_80.setter
    def time_80(self, value=None):
        """  Corresponds to IDD Field `time_80`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_80`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_80`')

        self._data["Time 80"] = value

    @property
    def value_until_time_80(self):
        """Get value_until_time_80

        Returns:
            float: the value of `value_until_time_80` or None if not set
        """
        return self._data["Value Until Time 80"]

    @value_until_time_80.setter
    def value_until_time_80(self, value=None):
        """  Corresponds to IDD Field `value_until_time_80`

        Args:
            value (float): value for IDD Field `value_until_time_80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_80`'.format(value))

        self._data["Value Until Time 80"] = value

    @property
    def time_81(self):
        """Get time_81

        Returns:
            str: the value of `time_81` or None if not set
        """
        return self._data["Time 81"]

    @time_81.setter
    def time_81(self, value=None):
        """  Corresponds to IDD Field `time_81`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_81`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_81`')

        self._data["Time 81"] = value

    @property
    def value_until_time_81(self):
        """Get value_until_time_81

        Returns:
            float: the value of `value_until_time_81` or None if not set
        """
        return self._data["Value Until Time 81"]

    @value_until_time_81.setter
    def value_until_time_81(self, value=None):
        """  Corresponds to IDD Field `value_until_time_81`

        Args:
            value (float): value for IDD Field `value_until_time_81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_81`'.format(value))

        self._data["Value Until Time 81"] = value

    @property
    def time_82(self):
        """Get time_82

        Returns:
            str: the value of `time_82` or None if not set
        """
        return self._data["Time 82"]

    @time_82.setter
    def time_82(self, value=None):
        """  Corresponds to IDD Field `time_82`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_82`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_82`')

        self._data["Time 82"] = value

    @property
    def value_until_time_82(self):
        """Get value_until_time_82

        Returns:
            float: the value of `value_until_time_82` or None if not set
        """
        return self._data["Value Until Time 82"]

    @value_until_time_82.setter
    def value_until_time_82(self, value=None):
        """  Corresponds to IDD Field `value_until_time_82`

        Args:
            value (float): value for IDD Field `value_until_time_82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_82`'.format(value))

        self._data["Value Until Time 82"] = value

    @property
    def time_83(self):
        """Get time_83

        Returns:
            str: the value of `time_83` or None if not set
        """
        return self._data["Time 83"]

    @time_83.setter
    def time_83(self, value=None):
        """  Corresponds to IDD Field `time_83`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_83`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_83`')

        self._data["Time 83"] = value

    @property
    def value_until_time_83(self):
        """Get value_until_time_83

        Returns:
            float: the value of `value_until_time_83` or None if not set
        """
        return self._data["Value Until Time 83"]

    @value_until_time_83.setter
    def value_until_time_83(self, value=None):
        """  Corresponds to IDD Field `value_until_time_83`

        Args:
            value (float): value for IDD Field `value_until_time_83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_83`'.format(value))

        self._data["Value Until Time 83"] = value

    @property
    def time_84(self):
        """Get time_84

        Returns:
            str: the value of `time_84` or None if not set
        """
        return self._data["Time 84"]

    @time_84.setter
    def time_84(self, value=None):
        """  Corresponds to IDD Field `time_84`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_84`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_84`')

        self._data["Time 84"] = value

    @property
    def value_until_time_84(self):
        """Get value_until_time_84

        Returns:
            float: the value of `value_until_time_84` or None if not set
        """
        return self._data["Value Until Time 84"]

    @value_until_time_84.setter
    def value_until_time_84(self, value=None):
        """  Corresponds to IDD Field `value_until_time_84`

        Args:
            value (float): value for IDD Field `value_until_time_84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_84`'.format(value))

        self._data["Value Until Time 84"] = value

    @property
    def time_85(self):
        """Get time_85

        Returns:
            str: the value of `time_85` or None if not set
        """
        return self._data["Time 85"]

    @time_85.setter
    def time_85(self, value=None):
        """  Corresponds to IDD Field `time_85`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_85`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_85`')

        self._data["Time 85"] = value

    @property
    def value_until_time_85(self):
        """Get value_until_time_85

        Returns:
            float: the value of `value_until_time_85` or None if not set
        """
        return self._data["Value Until Time 85"]

    @value_until_time_85.setter
    def value_until_time_85(self, value=None):
        """  Corresponds to IDD Field `value_until_time_85`

        Args:
            value (float): value for IDD Field `value_until_time_85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_85`'.format(value))

        self._data["Value Until Time 85"] = value

    @property
    def time_86(self):
        """Get time_86

        Returns:
            str: the value of `time_86` or None if not set
        """
        return self._data["Time 86"]

    @time_86.setter
    def time_86(self, value=None):
        """  Corresponds to IDD Field `time_86`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_86`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_86`')

        self._data["Time 86"] = value

    @property
    def value_until_time_86(self):
        """Get value_until_time_86

        Returns:
            float: the value of `value_until_time_86` or None if not set
        """
        return self._data["Value Until Time 86"]

    @value_until_time_86.setter
    def value_until_time_86(self, value=None):
        """  Corresponds to IDD Field `value_until_time_86`

        Args:
            value (float): value for IDD Field `value_until_time_86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_86`'.format(value))

        self._data["Value Until Time 86"] = value

    @property
    def time_87(self):
        """Get time_87

        Returns:
            str: the value of `time_87` or None if not set
        """
        return self._data["Time 87"]

    @time_87.setter
    def time_87(self, value=None):
        """  Corresponds to IDD Field `time_87`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_87`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_87`')

        self._data["Time 87"] = value

    @property
    def value_until_time_87(self):
        """Get value_until_time_87

        Returns:
            float: the value of `value_until_time_87` or None if not set
        """
        return self._data["Value Until Time 87"]

    @value_until_time_87.setter
    def value_until_time_87(self, value=None):
        """  Corresponds to IDD Field `value_until_time_87`

        Args:
            value (float): value for IDD Field `value_until_time_87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_87`'.format(value))

        self._data["Value Until Time 87"] = value

    @property
    def time_88(self):
        """Get time_88

        Returns:
            str: the value of `time_88` or None if not set
        """
        return self._data["Time 88"]

    @time_88.setter
    def time_88(self, value=None):
        """  Corresponds to IDD Field `time_88`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_88`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_88`')

        self._data["Time 88"] = value

    @property
    def value_until_time_88(self):
        """Get value_until_time_88

        Returns:
            float: the value of `value_until_time_88` or None if not set
        """
        return self._data["Value Until Time 88"]

    @value_until_time_88.setter
    def value_until_time_88(self, value=None):
        """  Corresponds to IDD Field `value_until_time_88`

        Args:
            value (float): value for IDD Field `value_until_time_88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_88`'.format(value))

        self._data["Value Until Time 88"] = value

    @property
    def time_89(self):
        """Get time_89

        Returns:
            str: the value of `time_89` or None if not set
        """
        return self._data["Time 89"]

    @time_89.setter
    def time_89(self, value=None):
        """  Corresponds to IDD Field `time_89`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_89`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_89`')

        self._data["Time 89"] = value

    @property
    def value_until_time_89(self):
        """Get value_until_time_89

        Returns:
            float: the value of `value_until_time_89` or None if not set
        """
        return self._data["Value Until Time 89"]

    @value_until_time_89.setter
    def value_until_time_89(self, value=None):
        """  Corresponds to IDD Field `value_until_time_89`

        Args:
            value (float): value for IDD Field `value_until_time_89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_89`'.format(value))

        self._data["Value Until Time 89"] = value

    @property
    def time_90(self):
        """Get time_90

        Returns:
            str: the value of `time_90` or None if not set
        """
        return self._data["Time 90"]

    @time_90.setter
    def time_90(self, value=None):
        """  Corresponds to IDD Field `time_90`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_90`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_90`')

        self._data["Time 90"] = value

    @property
    def value_until_time_90(self):
        """Get value_until_time_90

        Returns:
            float: the value of `value_until_time_90` or None if not set
        """
        return self._data["Value Until Time 90"]

    @value_until_time_90.setter
    def value_until_time_90(self, value=None):
        """  Corresponds to IDD Field `value_until_time_90`

        Args:
            value (float): value for IDD Field `value_until_time_90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_90`'.format(value))

        self._data["Value Until Time 90"] = value

    @property
    def time_91(self):
        """Get time_91

        Returns:
            str: the value of `time_91` or None if not set
        """
        return self._data["Time 91"]

    @time_91.setter
    def time_91(self, value=None):
        """  Corresponds to IDD Field `time_91`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_91`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_91`')

        self._data["Time 91"] = value

    @property
    def value_until_time_91(self):
        """Get value_until_time_91

        Returns:
            float: the value of `value_until_time_91` or None if not set
        """
        return self._data["Value Until Time 91"]

    @value_until_time_91.setter
    def value_until_time_91(self, value=None):
        """  Corresponds to IDD Field `value_until_time_91`

        Args:
            value (float): value for IDD Field `value_until_time_91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_91`'.format(value))

        self._data["Value Until Time 91"] = value

    @property
    def time_92(self):
        """Get time_92

        Returns:
            str: the value of `time_92` or None if not set
        """
        return self._data["Time 92"]

    @time_92.setter
    def time_92(self, value=None):
        """  Corresponds to IDD Field `time_92`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_92`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_92`')

        self._data["Time 92"] = value

    @property
    def value_until_time_92(self):
        """Get value_until_time_92

        Returns:
            float: the value of `value_until_time_92` or None if not set
        """
        return self._data["Value Until Time 92"]

    @value_until_time_92.setter
    def value_until_time_92(self, value=None):
        """  Corresponds to IDD Field `value_until_time_92`

        Args:
            value (float): value for IDD Field `value_until_time_92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_92`'.format(value))

        self._data["Value Until Time 92"] = value

    @property
    def time_93(self):
        """Get time_93

        Returns:
            str: the value of `time_93` or None if not set
        """
        return self._data["Time 93"]

    @time_93.setter
    def time_93(self, value=None):
        """  Corresponds to IDD Field `time_93`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_93`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_93`')

        self._data["Time 93"] = value

    @property
    def value_until_time_93(self):
        """Get value_until_time_93

        Returns:
            float: the value of `value_until_time_93` or None if not set
        """
        return self._data["Value Until Time 93"]

    @value_until_time_93.setter
    def value_until_time_93(self, value=None):
        """  Corresponds to IDD Field `value_until_time_93`

        Args:
            value (float): value for IDD Field `value_until_time_93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_93`'.format(value))

        self._data["Value Until Time 93"] = value

    @property
    def time_94(self):
        """Get time_94

        Returns:
            str: the value of `time_94` or None if not set
        """
        return self._data["Time 94"]

    @time_94.setter
    def time_94(self, value=None):
        """  Corresponds to IDD Field `time_94`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_94`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_94`')

        self._data["Time 94"] = value

    @property
    def value_until_time_94(self):
        """Get value_until_time_94

        Returns:
            float: the value of `value_until_time_94` or None if not set
        """
        return self._data["Value Until Time 94"]

    @value_until_time_94.setter
    def value_until_time_94(self, value=None):
        """  Corresponds to IDD Field `value_until_time_94`

        Args:
            value (float): value for IDD Field `value_until_time_94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_94`'.format(value))

        self._data["Value Until Time 94"] = value

    @property
    def time_95(self):
        """Get time_95

        Returns:
            str: the value of `time_95` or None if not set
        """
        return self._data["Time 95"]

    @time_95.setter
    def time_95(self, value=None):
        """  Corresponds to IDD Field `time_95`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_95`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_95`')

        self._data["Time 95"] = value

    @property
    def value_until_time_95(self):
        """Get value_until_time_95

        Returns:
            float: the value of `value_until_time_95` or None if not set
        """
        return self._data["Value Until Time 95"]

    @value_until_time_95.setter
    def value_until_time_95(self, value=None):
        """  Corresponds to IDD Field `value_until_time_95`

        Args:
            value (float): value for IDD Field `value_until_time_95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_95`'.format(value))

        self._data["Value Until Time 95"] = value

    @property
    def time_96(self):
        """Get time_96

        Returns:
            str: the value of `time_96` or None if not set
        """
        return self._data["Time 96"]

    @time_96.setter
    def time_96(self, value=None):
        """  Corresponds to IDD Field `time_96`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_96`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_96`')

        self._data["Time 96"] = value

    @property
    def value_until_time_96(self):
        """Get value_until_time_96

        Returns:
            float: the value of `value_until_time_96` or None if not set
        """
        return self._data["Value Until Time 96"]

    @value_until_time_96.setter
    def value_until_time_96(self, value=None):
        """  Corresponds to IDD Field `value_until_time_96`

        Args:
            value (float): value for IDD Field `value_until_time_96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_96`'.format(value))

        self._data["Value Until Time 96"] = value

    @property
    def time_97(self):
        """Get time_97

        Returns:
            str: the value of `time_97` or None if not set
        """
        return self._data["Time 97"]

    @time_97.setter
    def time_97(self, value=None):
        """  Corresponds to IDD Field `time_97`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_97`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_97`')

        self._data["Time 97"] = value

    @property
    def value_until_time_97(self):
        """Get value_until_time_97

        Returns:
            float: the value of `value_until_time_97` or None if not set
        """
        return self._data["Value Until Time 97"]

    @value_until_time_97.setter
    def value_until_time_97(self, value=None):
        """  Corresponds to IDD Field `value_until_time_97`

        Args:
            value (float): value for IDD Field `value_until_time_97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_97`'.format(value))

        self._data["Value Until Time 97"] = value

    @property
    def time_98(self):
        """Get time_98

        Returns:
            str: the value of `time_98` or None if not set
        """
        return self._data["Time 98"]

    @time_98.setter
    def time_98(self, value=None):
        """  Corresponds to IDD Field `time_98`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_98`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_98`')

        self._data["Time 98"] = value

    @property
    def value_until_time_98(self):
        """Get value_until_time_98

        Returns:
            float: the value of `value_until_time_98` or None if not set
        """
        return self._data["Value Until Time 98"]

    @value_until_time_98.setter
    def value_until_time_98(self, value=None):
        """  Corresponds to IDD Field `value_until_time_98`

        Args:
            value (float): value for IDD Field `value_until_time_98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_98`'.format(value))

        self._data["Value Until Time 98"] = value

    @property
    def time_99(self):
        """Get time_99

        Returns:
            str: the value of `time_99` or None if not set
        """
        return self._data["Time 99"]

    @time_99.setter
    def time_99(self, value=None):
        """  Corresponds to IDD Field `time_99`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_99`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_99`')

        self._data["Time 99"] = value

    @property
    def value_until_time_99(self):
        """Get value_until_time_99

        Returns:
            float: the value of `value_until_time_99` or None if not set
        """
        return self._data["Value Until Time 99"]

    @value_until_time_99.setter
    def value_until_time_99(self, value=None):
        """  Corresponds to IDD Field `value_until_time_99`

        Args:
            value (float): value for IDD Field `value_until_time_99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_99`'.format(value))

        self._data["Value Until Time 99"] = value

    @property
    def time_100(self):
        """Get time_100

        Returns:
            str: the value of `time_100` or None if not set
        """
        return self._data["Time 100"]

    @time_100.setter
    def time_100(self, value=None):
        """  Corresponds to IDD Field `time_100`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_100`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_100`')

        self._data["Time 100"] = value

    @property
    def value_until_time_100(self):
        """Get value_until_time_100

        Returns:
            float: the value of `value_until_time_100` or None if not set
        """
        return self._data["Value Until Time 100"]

    @value_until_time_100.setter
    def value_until_time_100(self, value=None):
        """  Corresponds to IDD Field `value_until_time_100`

        Args:
            value (float): value for IDD Field `value_until_time_100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_100`'.format(value))

        self._data["Value Until Time 100"] = value

    @property
    def time_101(self):
        """Get time_101

        Returns:
            str: the value of `time_101` or None if not set
        """
        return self._data["Time 101"]

    @time_101.setter
    def time_101(self, value=None):
        """  Corresponds to IDD Field `time_101`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_101`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_101`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_101`')

        self._data["Time 101"] = value

    @property
    def value_until_time_101(self):
        """Get value_until_time_101

        Returns:
            float: the value of `value_until_time_101` or None if not set
        """
        return self._data["Value Until Time 101"]

    @value_until_time_101.setter
    def value_until_time_101(self, value=None):
        """  Corresponds to IDD Field `value_until_time_101`

        Args:
            value (float): value for IDD Field `value_until_time_101`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_101`'.format(value))

        self._data["Value Until Time 101"] = value

    @property
    def time_102(self):
        """Get time_102

        Returns:
            str: the value of `time_102` or None if not set
        """
        return self._data["Time 102"]

    @time_102.setter
    def time_102(self, value=None):
        """  Corresponds to IDD Field `time_102`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_102`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_102`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_102`')

        self._data["Time 102"] = value

    @property
    def value_until_time_102(self):
        """Get value_until_time_102

        Returns:
            float: the value of `value_until_time_102` or None if not set
        """
        return self._data["Value Until Time 102"]

    @value_until_time_102.setter
    def value_until_time_102(self, value=None):
        """  Corresponds to IDD Field `value_until_time_102`

        Args:
            value (float): value for IDD Field `value_until_time_102`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_102`'.format(value))

        self._data["Value Until Time 102"] = value

    @property
    def time_103(self):
        """Get time_103

        Returns:
            str: the value of `time_103` or None if not set
        """
        return self._data["Time 103"]

    @time_103.setter
    def time_103(self, value=None):
        """  Corresponds to IDD Field `time_103`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_103`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_103`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_103`')

        self._data["Time 103"] = value

    @property
    def value_until_time_103(self):
        """Get value_until_time_103

        Returns:
            float: the value of `value_until_time_103` or None if not set
        """
        return self._data["Value Until Time 103"]

    @value_until_time_103.setter
    def value_until_time_103(self, value=None):
        """  Corresponds to IDD Field `value_until_time_103`

        Args:
            value (float): value for IDD Field `value_until_time_103`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_103`'.format(value))

        self._data["Value Until Time 103"] = value

    @property
    def time_104(self):
        """Get time_104

        Returns:
            str: the value of `time_104` or None if not set
        """
        return self._data["Time 104"]

    @time_104.setter
    def time_104(self, value=None):
        """  Corresponds to IDD Field `time_104`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_104`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_104`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_104`')

        self._data["Time 104"] = value

    @property
    def value_until_time_104(self):
        """Get value_until_time_104

        Returns:
            float: the value of `value_until_time_104` or None if not set
        """
        return self._data["Value Until Time 104"]

    @value_until_time_104.setter
    def value_until_time_104(self, value=None):
        """  Corresponds to IDD Field `value_until_time_104`

        Args:
            value (float): value for IDD Field `value_until_time_104`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_104`'.format(value))

        self._data["Value Until Time 104"] = value

    @property
    def time_105(self):
        """Get time_105

        Returns:
            str: the value of `time_105` or None if not set
        """
        return self._data["Time 105"]

    @time_105.setter
    def time_105(self, value=None):
        """  Corresponds to IDD Field `time_105`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_105`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_105`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_105`')

        self._data["Time 105"] = value

    @property
    def value_until_time_105(self):
        """Get value_until_time_105

        Returns:
            float: the value of `value_until_time_105` or None if not set
        """
        return self._data["Value Until Time 105"]

    @value_until_time_105.setter
    def value_until_time_105(self, value=None):
        """  Corresponds to IDD Field `value_until_time_105`

        Args:
            value (float): value for IDD Field `value_until_time_105`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_105`'.format(value))

        self._data["Value Until Time 105"] = value

    @property
    def time_106(self):
        """Get time_106

        Returns:
            str: the value of `time_106` or None if not set
        """
        return self._data["Time 106"]

    @time_106.setter
    def time_106(self, value=None):
        """  Corresponds to IDD Field `time_106`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_106`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_106`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_106`')

        self._data["Time 106"] = value

    @property
    def value_until_time_106(self):
        """Get value_until_time_106

        Returns:
            float: the value of `value_until_time_106` or None if not set
        """
        return self._data["Value Until Time 106"]

    @value_until_time_106.setter
    def value_until_time_106(self, value=None):
        """  Corresponds to IDD Field `value_until_time_106`

        Args:
            value (float): value for IDD Field `value_until_time_106`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_106`'.format(value))

        self._data["Value Until Time 106"] = value

    @property
    def time_107(self):
        """Get time_107

        Returns:
            str: the value of `time_107` or None if not set
        """
        return self._data["Time 107"]

    @time_107.setter
    def time_107(self, value=None):
        """  Corresponds to IDD Field `time_107`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_107`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_107`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_107`')

        self._data["Time 107"] = value

    @property
    def value_until_time_107(self):
        """Get value_until_time_107

        Returns:
            float: the value of `value_until_time_107` or None if not set
        """
        return self._data["Value Until Time 107"]

    @value_until_time_107.setter
    def value_until_time_107(self, value=None):
        """  Corresponds to IDD Field `value_until_time_107`

        Args:
            value (float): value for IDD Field `value_until_time_107`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_107`'.format(value))

        self._data["Value Until Time 107"] = value

    @property
    def time_108(self):
        """Get time_108

        Returns:
            str: the value of `time_108` or None if not set
        """
        return self._data["Time 108"]

    @time_108.setter
    def time_108(self, value=None):
        """  Corresponds to IDD Field `time_108`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_108`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_108`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_108`')

        self._data["Time 108"] = value

    @property
    def value_until_time_108(self):
        """Get value_until_time_108

        Returns:
            float: the value of `value_until_time_108` or None if not set
        """
        return self._data["Value Until Time 108"]

    @value_until_time_108.setter
    def value_until_time_108(self, value=None):
        """  Corresponds to IDD Field `value_until_time_108`

        Args:
            value (float): value for IDD Field `value_until_time_108`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_108`'.format(value))

        self._data["Value Until Time 108"] = value

    @property
    def time_109(self):
        """Get time_109

        Returns:
            str: the value of `time_109` or None if not set
        """
        return self._data["Time 109"]

    @time_109.setter
    def time_109(self, value=None):
        """  Corresponds to IDD Field `time_109`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_109`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_109`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_109`')

        self._data["Time 109"] = value

    @property
    def value_until_time_109(self):
        """Get value_until_time_109

        Returns:
            float: the value of `value_until_time_109` or None if not set
        """
        return self._data["Value Until Time 109"]

    @value_until_time_109.setter
    def value_until_time_109(self, value=None):
        """  Corresponds to IDD Field `value_until_time_109`

        Args:
            value (float): value for IDD Field `value_until_time_109`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_109`'.format(value))

        self._data["Value Until Time 109"] = value

    @property
    def time_110(self):
        """Get time_110

        Returns:
            str: the value of `time_110` or None if not set
        """
        return self._data["Time 110"]

    @time_110.setter
    def time_110(self, value=None):
        """  Corresponds to IDD Field `time_110`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_110`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_110`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_110`')

        self._data["Time 110"] = value

    @property
    def value_until_time_110(self):
        """Get value_until_time_110

        Returns:
            float: the value of `value_until_time_110` or None if not set
        """
        return self._data["Value Until Time 110"]

    @value_until_time_110.setter
    def value_until_time_110(self, value=None):
        """  Corresponds to IDD Field `value_until_time_110`

        Args:
            value (float): value for IDD Field `value_until_time_110`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_110`'.format(value))

        self._data["Value Until Time 110"] = value

    @property
    def time_111(self):
        """Get time_111

        Returns:
            str: the value of `time_111` or None if not set
        """
        return self._data["Time 111"]

    @time_111.setter
    def time_111(self, value=None):
        """  Corresponds to IDD Field `time_111`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_111`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_111`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_111`')

        self._data["Time 111"] = value

    @property
    def value_until_time_111(self):
        """Get value_until_time_111

        Returns:
            float: the value of `value_until_time_111` or None if not set
        """
        return self._data["Value Until Time 111"]

    @value_until_time_111.setter
    def value_until_time_111(self, value=None):
        """  Corresponds to IDD Field `value_until_time_111`

        Args:
            value (float): value for IDD Field `value_until_time_111`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_111`'.format(value))

        self._data["Value Until Time 111"] = value

    @property
    def time_112(self):
        """Get time_112

        Returns:
            str: the value of `time_112` or None if not set
        """
        return self._data["Time 112"]

    @time_112.setter
    def time_112(self, value=None):
        """  Corresponds to IDD Field `time_112`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_112`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_112`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_112`')

        self._data["Time 112"] = value

    @property
    def value_until_time_112(self):
        """Get value_until_time_112

        Returns:
            float: the value of `value_until_time_112` or None if not set
        """
        return self._data["Value Until Time 112"]

    @value_until_time_112.setter
    def value_until_time_112(self, value=None):
        """  Corresponds to IDD Field `value_until_time_112`

        Args:
            value (float): value for IDD Field `value_until_time_112`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_112`'.format(value))

        self._data["Value Until Time 112"] = value

    @property
    def time_113(self):
        """Get time_113

        Returns:
            str: the value of `time_113` or None if not set
        """
        return self._data["Time 113"]

    @time_113.setter
    def time_113(self, value=None):
        """  Corresponds to IDD Field `time_113`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_113`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_113`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_113`')

        self._data["Time 113"] = value

    @property
    def value_until_time_113(self):
        """Get value_until_time_113

        Returns:
            float: the value of `value_until_time_113` or None if not set
        """
        return self._data["Value Until Time 113"]

    @value_until_time_113.setter
    def value_until_time_113(self, value=None):
        """  Corresponds to IDD Field `value_until_time_113`

        Args:
            value (float): value for IDD Field `value_until_time_113`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_113`'.format(value))

        self._data["Value Until Time 113"] = value

    @property
    def time_114(self):
        """Get time_114

        Returns:
            str: the value of `time_114` or None if not set
        """
        return self._data["Time 114"]

    @time_114.setter
    def time_114(self, value=None):
        """  Corresponds to IDD Field `time_114`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_114`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_114`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_114`')

        self._data["Time 114"] = value

    @property
    def value_until_time_114(self):
        """Get value_until_time_114

        Returns:
            float: the value of `value_until_time_114` or None if not set
        """
        return self._data["Value Until Time 114"]

    @value_until_time_114.setter
    def value_until_time_114(self, value=None):
        """  Corresponds to IDD Field `value_until_time_114`

        Args:
            value (float): value for IDD Field `value_until_time_114`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_114`'.format(value))

        self._data["Value Until Time 114"] = value

    @property
    def time_115(self):
        """Get time_115

        Returns:
            str: the value of `time_115` or None if not set
        """
        return self._data["Time 115"]

    @time_115.setter
    def time_115(self, value=None):
        """  Corresponds to IDD Field `time_115`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_115`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_115`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_115`')

        self._data["Time 115"] = value

    @property
    def value_until_time_115(self):
        """Get value_until_time_115

        Returns:
            float: the value of `value_until_time_115` or None if not set
        """
        return self._data["Value Until Time 115"]

    @value_until_time_115.setter
    def value_until_time_115(self, value=None):
        """  Corresponds to IDD Field `value_until_time_115`

        Args:
            value (float): value for IDD Field `value_until_time_115`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_115`'.format(value))

        self._data["Value Until Time 115"] = value

    @property
    def time_116(self):
        """Get time_116

        Returns:
            str: the value of `time_116` or None if not set
        """
        return self._data["Time 116"]

    @time_116.setter
    def time_116(self, value=None):
        """  Corresponds to IDD Field `time_116`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_116`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_116`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_116`')

        self._data["Time 116"] = value

    @property
    def value_until_time_116(self):
        """Get value_until_time_116

        Returns:
            float: the value of `value_until_time_116` or None if not set
        """
        return self._data["Value Until Time 116"]

    @value_until_time_116.setter
    def value_until_time_116(self, value=None):
        """  Corresponds to IDD Field `value_until_time_116`

        Args:
            value (float): value for IDD Field `value_until_time_116`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_116`'.format(value))

        self._data["Value Until Time 116"] = value

    @property
    def time_117(self):
        """Get time_117

        Returns:
            str: the value of `time_117` or None if not set
        """
        return self._data["Time 117"]

    @time_117.setter
    def time_117(self, value=None):
        """  Corresponds to IDD Field `time_117`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_117`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_117`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_117`')

        self._data["Time 117"] = value

    @property
    def value_until_time_117(self):
        """Get value_until_time_117

        Returns:
            float: the value of `value_until_time_117` or None if not set
        """
        return self._data["Value Until Time 117"]

    @value_until_time_117.setter
    def value_until_time_117(self, value=None):
        """  Corresponds to IDD Field `value_until_time_117`

        Args:
            value (float): value for IDD Field `value_until_time_117`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_117`'.format(value))

        self._data["Value Until Time 117"] = value

    @property
    def time_118(self):
        """Get time_118

        Returns:
            str: the value of `time_118` or None if not set
        """
        return self._data["Time 118"]

    @time_118.setter
    def time_118(self, value=None):
        """  Corresponds to IDD Field `time_118`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_118`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_118`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_118`')

        self._data["Time 118"] = value

    @property
    def value_until_time_118(self):
        """Get value_until_time_118

        Returns:
            float: the value of `value_until_time_118` or None if not set
        """
        return self._data["Value Until Time 118"]

    @value_until_time_118.setter
    def value_until_time_118(self, value=None):
        """  Corresponds to IDD Field `value_until_time_118`

        Args:
            value (float): value for IDD Field `value_until_time_118`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_118`'.format(value))

        self._data["Value Until Time 118"] = value

    @property
    def time_119(self):
        """Get time_119

        Returns:
            str: the value of `time_119` or None if not set
        """
        return self._data["Time 119"]

    @time_119.setter
    def time_119(self, value=None):
        """  Corresponds to IDD Field `time_119`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_119`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_119`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_119`')

        self._data["Time 119"] = value

    @property
    def value_until_time_119(self):
        """Get value_until_time_119

        Returns:
            float: the value of `value_until_time_119` or None if not set
        """
        return self._data["Value Until Time 119"]

    @value_until_time_119.setter
    def value_until_time_119(self, value=None):
        """  Corresponds to IDD Field `value_until_time_119`

        Args:
            value (float): value for IDD Field `value_until_time_119`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_119`'.format(value))

        self._data["Value Until Time 119"] = value

    @property
    def time_120(self):
        """Get time_120

        Returns:
            str: the value of `time_120` or None if not set
        """
        return self._data["Time 120"]

    @time_120.setter
    def time_120(self, value=None):
        """  Corresponds to IDD Field `time_120`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_120`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_120`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_120`')

        self._data["Time 120"] = value

    @property
    def value_until_time_120(self):
        """Get value_until_time_120

        Returns:
            float: the value of `value_until_time_120` or None if not set
        """
        return self._data["Value Until Time 120"]

    @value_until_time_120.setter
    def value_until_time_120(self, value=None):
        """  Corresponds to IDD Field `value_until_time_120`

        Args:
            value (float): value for IDD Field `value_until_time_120`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_120`'.format(value))

        self._data["Value Until Time 120"] = value

    @property
    def time_121(self):
        """Get time_121

        Returns:
            str: the value of `time_121` or None if not set
        """
        return self._data["Time 121"]

    @time_121.setter
    def time_121(self, value=None):
        """  Corresponds to IDD Field `time_121`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_121`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_121`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_121`')

        self._data["Time 121"] = value

    @property
    def value_until_time_121(self):
        """Get value_until_time_121

        Returns:
            float: the value of `value_until_time_121` or None if not set
        """
        return self._data["Value Until Time 121"]

    @value_until_time_121.setter
    def value_until_time_121(self, value=None):
        """  Corresponds to IDD Field `value_until_time_121`

        Args:
            value (float): value for IDD Field `value_until_time_121`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_121`'.format(value))

        self._data["Value Until Time 121"] = value

    @property
    def time_122(self):
        """Get time_122

        Returns:
            str: the value of `time_122` or None if not set
        """
        return self._data["Time 122"]

    @time_122.setter
    def time_122(self, value=None):
        """  Corresponds to IDD Field `time_122`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_122`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_122`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_122`')

        self._data["Time 122"] = value

    @property
    def value_until_time_122(self):
        """Get value_until_time_122

        Returns:
            float: the value of `value_until_time_122` or None if not set
        """
        return self._data["Value Until Time 122"]

    @value_until_time_122.setter
    def value_until_time_122(self, value=None):
        """  Corresponds to IDD Field `value_until_time_122`

        Args:
            value (float): value for IDD Field `value_until_time_122`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_122`'.format(value))

        self._data["Value Until Time 122"] = value

    @property
    def time_123(self):
        """Get time_123

        Returns:
            str: the value of `time_123` or None if not set
        """
        return self._data["Time 123"]

    @time_123.setter
    def time_123(self, value=None):
        """  Corresponds to IDD Field `time_123`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_123`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_123`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_123`')

        self._data["Time 123"] = value

    @property
    def value_until_time_123(self):
        """Get value_until_time_123

        Returns:
            float: the value of `value_until_time_123` or None if not set
        """
        return self._data["Value Until Time 123"]

    @value_until_time_123.setter
    def value_until_time_123(self, value=None):
        """  Corresponds to IDD Field `value_until_time_123`

        Args:
            value (float): value for IDD Field `value_until_time_123`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_123`'.format(value))

        self._data["Value Until Time 123"] = value

    @property
    def time_124(self):
        """Get time_124

        Returns:
            str: the value of `time_124` or None if not set
        """
        return self._data["Time 124"]

    @time_124.setter
    def time_124(self, value=None):
        """  Corresponds to IDD Field `time_124`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_124`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_124`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_124`')

        self._data["Time 124"] = value

    @property
    def value_until_time_124(self):
        """Get value_until_time_124

        Returns:
            float: the value of `value_until_time_124` or None if not set
        """
        return self._data["Value Until Time 124"]

    @value_until_time_124.setter
    def value_until_time_124(self, value=None):
        """  Corresponds to IDD Field `value_until_time_124`

        Args:
            value (float): value for IDD Field `value_until_time_124`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_124`'.format(value))

        self._data["Value Until Time 124"] = value

    @property
    def time_125(self):
        """Get time_125

        Returns:
            str: the value of `time_125` or None if not set
        """
        return self._data["Time 125"]

    @time_125.setter
    def time_125(self, value=None):
        """  Corresponds to IDD Field `time_125`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_125`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_125`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_125`')

        self._data["Time 125"] = value

    @property
    def value_until_time_125(self):
        """Get value_until_time_125

        Returns:
            float: the value of `value_until_time_125` or None if not set
        """
        return self._data["Value Until Time 125"]

    @value_until_time_125.setter
    def value_until_time_125(self, value=None):
        """  Corresponds to IDD Field `value_until_time_125`

        Args:
            value (float): value for IDD Field `value_until_time_125`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_125`'.format(value))

        self._data["Value Until Time 125"] = value

    @property
    def time_126(self):
        """Get time_126

        Returns:
            str: the value of `time_126` or None if not set
        """
        return self._data["Time 126"]

    @time_126.setter
    def time_126(self, value=None):
        """  Corresponds to IDD Field `time_126`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_126`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_126`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_126`')

        self._data["Time 126"] = value

    @property
    def value_until_time_126(self):
        """Get value_until_time_126

        Returns:
            float: the value of `value_until_time_126` or None if not set
        """
        return self._data["Value Until Time 126"]

    @value_until_time_126.setter
    def value_until_time_126(self, value=None):
        """  Corresponds to IDD Field `value_until_time_126`

        Args:
            value (float): value for IDD Field `value_until_time_126`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_126`'.format(value))

        self._data["Value Until Time 126"] = value

    @property
    def time_127(self):
        """Get time_127

        Returns:
            str: the value of `time_127` or None if not set
        """
        return self._data["Time 127"]

    @time_127.setter
    def time_127(self, value=None):
        """  Corresponds to IDD Field `time_127`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_127`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_127`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_127`')

        self._data["Time 127"] = value

    @property
    def value_until_time_127(self):
        """Get value_until_time_127

        Returns:
            float: the value of `value_until_time_127` or None if not set
        """
        return self._data["Value Until Time 127"]

    @value_until_time_127.setter
    def value_until_time_127(self, value=None):
        """  Corresponds to IDD Field `value_until_time_127`

        Args:
            value (float): value for IDD Field `value_until_time_127`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_127`'.format(value))

        self._data["Value Until Time 127"] = value

    @property
    def time_128(self):
        """Get time_128

        Returns:
            str: the value of `time_128` or None if not set
        """
        return self._data["Time 128"]

    @time_128.setter
    def time_128(self, value=None):
        """  Corresponds to IDD Field `time_128`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_128`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_128`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_128`')

        self._data["Time 128"] = value

    @property
    def value_until_time_128(self):
        """Get value_until_time_128

        Returns:
            float: the value of `value_until_time_128` or None if not set
        """
        return self._data["Value Until Time 128"]

    @value_until_time_128.setter
    def value_until_time_128(self, value=None):
        """  Corresponds to IDD Field `value_until_time_128`

        Args:
            value (float): value for IDD Field `value_until_time_128`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_128`'.format(value))

        self._data["Value Until Time 128"] = value

    @property
    def time_129(self):
        """Get time_129

        Returns:
            str: the value of `time_129` or None if not set
        """
        return self._data["Time 129"]

    @time_129.setter
    def time_129(self, value=None):
        """  Corresponds to IDD Field `time_129`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_129`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_129`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_129`')

        self._data["Time 129"] = value

    @property
    def value_until_time_129(self):
        """Get value_until_time_129

        Returns:
            float: the value of `value_until_time_129` or None if not set
        """
        return self._data["Value Until Time 129"]

    @value_until_time_129.setter
    def value_until_time_129(self, value=None):
        """  Corresponds to IDD Field `value_until_time_129`

        Args:
            value (float): value for IDD Field `value_until_time_129`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_129`'.format(value))

        self._data["Value Until Time 129"] = value

    @property
    def time_130(self):
        """Get time_130

        Returns:
            str: the value of `time_130` or None if not set
        """
        return self._data["Time 130"]

    @time_130.setter
    def time_130(self, value=None):
        """  Corresponds to IDD Field `time_130`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_130`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_130`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_130`')

        self._data["Time 130"] = value

    @property
    def value_until_time_130(self):
        """Get value_until_time_130

        Returns:
            float: the value of `value_until_time_130` or None if not set
        """
        return self._data["Value Until Time 130"]

    @value_until_time_130.setter
    def value_until_time_130(self, value=None):
        """  Corresponds to IDD Field `value_until_time_130`

        Args:
            value (float): value for IDD Field `value_until_time_130`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_130`'.format(value))

        self._data["Value Until Time 130"] = value

    @property
    def time_131(self):
        """Get time_131

        Returns:
            str: the value of `time_131` or None if not set
        """
        return self._data["Time 131"]

    @time_131.setter
    def time_131(self, value=None):
        """  Corresponds to IDD Field `time_131`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_131`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_131`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_131`')

        self._data["Time 131"] = value

    @property
    def value_until_time_131(self):
        """Get value_until_time_131

        Returns:
            float: the value of `value_until_time_131` or None if not set
        """
        return self._data["Value Until Time 131"]

    @value_until_time_131.setter
    def value_until_time_131(self, value=None):
        """  Corresponds to IDD Field `value_until_time_131`

        Args:
            value (float): value for IDD Field `value_until_time_131`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_131`'.format(value))

        self._data["Value Until Time 131"] = value

    @property
    def time_132(self):
        """Get time_132

        Returns:
            str: the value of `time_132` or None if not set
        """
        return self._data["Time 132"]

    @time_132.setter
    def time_132(self, value=None):
        """  Corresponds to IDD Field `time_132`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_132`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_132`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_132`')

        self._data["Time 132"] = value

    @property
    def value_until_time_132(self):
        """Get value_until_time_132

        Returns:
            float: the value of `value_until_time_132` or None if not set
        """
        return self._data["Value Until Time 132"]

    @value_until_time_132.setter
    def value_until_time_132(self, value=None):
        """  Corresponds to IDD Field `value_until_time_132`

        Args:
            value (float): value for IDD Field `value_until_time_132`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_132`'.format(value))

        self._data["Value Until Time 132"] = value

    @property
    def time_133(self):
        """Get time_133

        Returns:
            str: the value of `time_133` or None if not set
        """
        return self._data["Time 133"]

    @time_133.setter
    def time_133(self, value=None):
        """  Corresponds to IDD Field `time_133`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_133`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_133`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_133`')

        self._data["Time 133"] = value

    @property
    def value_until_time_133(self):
        """Get value_until_time_133

        Returns:
            float: the value of `value_until_time_133` or None if not set
        """
        return self._data["Value Until Time 133"]

    @value_until_time_133.setter
    def value_until_time_133(self, value=None):
        """  Corresponds to IDD Field `value_until_time_133`

        Args:
            value (float): value for IDD Field `value_until_time_133`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_133`'.format(value))

        self._data["Value Until Time 133"] = value

    @property
    def time_134(self):
        """Get time_134

        Returns:
            str: the value of `time_134` or None if not set
        """
        return self._data["Time 134"]

    @time_134.setter
    def time_134(self, value=None):
        """  Corresponds to IDD Field `time_134`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_134`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_134`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_134`')

        self._data["Time 134"] = value

    @property
    def value_until_time_134(self):
        """Get value_until_time_134

        Returns:
            float: the value of `value_until_time_134` or None if not set
        """
        return self._data["Value Until Time 134"]

    @value_until_time_134.setter
    def value_until_time_134(self, value=None):
        """  Corresponds to IDD Field `value_until_time_134`

        Args:
            value (float): value for IDD Field `value_until_time_134`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_134`'.format(value))

        self._data["Value Until Time 134"] = value

    @property
    def time_135(self):
        """Get time_135

        Returns:
            str: the value of `time_135` or None if not set
        """
        return self._data["Time 135"]

    @time_135.setter
    def time_135(self, value=None):
        """  Corresponds to IDD Field `time_135`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_135`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_135`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_135`')

        self._data["Time 135"] = value

    @property
    def value_until_time_135(self):
        """Get value_until_time_135

        Returns:
            float: the value of `value_until_time_135` or None if not set
        """
        return self._data["Value Until Time 135"]

    @value_until_time_135.setter
    def value_until_time_135(self, value=None):
        """  Corresponds to IDD Field `value_until_time_135`

        Args:
            value (float): value for IDD Field `value_until_time_135`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_135`'.format(value))

        self._data["Value Until Time 135"] = value

    @property
    def time_136(self):
        """Get time_136

        Returns:
            str: the value of `time_136` or None if not set
        """
        return self._data["Time 136"]

    @time_136.setter
    def time_136(self, value=None):
        """  Corresponds to IDD Field `time_136`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_136`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_136`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_136`')

        self._data["Time 136"] = value

    @property
    def value_until_time_136(self):
        """Get value_until_time_136

        Returns:
            float: the value of `value_until_time_136` or None if not set
        """
        return self._data["Value Until Time 136"]

    @value_until_time_136.setter
    def value_until_time_136(self, value=None):
        """  Corresponds to IDD Field `value_until_time_136`

        Args:
            value (float): value for IDD Field `value_until_time_136`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_136`'.format(value))

        self._data["Value Until Time 136"] = value

    @property
    def time_137(self):
        """Get time_137

        Returns:
            str: the value of `time_137` or None if not set
        """
        return self._data["Time 137"]

    @time_137.setter
    def time_137(self, value=None):
        """  Corresponds to IDD Field `time_137`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_137`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_137`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_137`')

        self._data["Time 137"] = value

    @property
    def value_until_time_137(self):
        """Get value_until_time_137

        Returns:
            float: the value of `value_until_time_137` or None if not set
        """
        return self._data["Value Until Time 137"]

    @value_until_time_137.setter
    def value_until_time_137(self, value=None):
        """  Corresponds to IDD Field `value_until_time_137`

        Args:
            value (float): value for IDD Field `value_until_time_137`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_137`'.format(value))

        self._data["Value Until Time 137"] = value

    @property
    def time_138(self):
        """Get time_138

        Returns:
            str: the value of `time_138` or None if not set
        """
        return self._data["Time 138"]

    @time_138.setter
    def time_138(self, value=None):
        """  Corresponds to IDD Field `time_138`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_138`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_138`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_138`')

        self._data["Time 138"] = value

    @property
    def value_until_time_138(self):
        """Get value_until_time_138

        Returns:
            float: the value of `value_until_time_138` or None if not set
        """
        return self._data["Value Until Time 138"]

    @value_until_time_138.setter
    def value_until_time_138(self, value=None):
        """  Corresponds to IDD Field `value_until_time_138`

        Args:
            value (float): value for IDD Field `value_until_time_138`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_138`'.format(value))

        self._data["Value Until Time 138"] = value

    @property
    def time_139(self):
        """Get time_139

        Returns:
            str: the value of `time_139` or None if not set
        """
        return self._data["Time 139"]

    @time_139.setter
    def time_139(self, value=None):
        """  Corresponds to IDD Field `time_139`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_139`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_139`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_139`')

        self._data["Time 139"] = value

    @property
    def value_until_time_139(self):
        """Get value_until_time_139

        Returns:
            float: the value of `value_until_time_139` or None if not set
        """
        return self._data["Value Until Time 139"]

    @value_until_time_139.setter
    def value_until_time_139(self, value=None):
        """  Corresponds to IDD Field `value_until_time_139`

        Args:
            value (float): value for IDD Field `value_until_time_139`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_139`'.format(value))

        self._data["Value Until Time 139"] = value

    @property
    def time_140(self):
        """Get time_140

        Returns:
            str: the value of `time_140` or None if not set
        """
        return self._data["Time 140"]

    @time_140.setter
    def time_140(self, value=None):
        """  Corresponds to IDD Field `time_140`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_140`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_140`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_140`')

        self._data["Time 140"] = value

    @property
    def value_until_time_140(self):
        """Get value_until_time_140

        Returns:
            float: the value of `value_until_time_140` or None if not set
        """
        return self._data["Value Until Time 140"]

    @value_until_time_140.setter
    def value_until_time_140(self, value=None):
        """  Corresponds to IDD Field `value_until_time_140`

        Args:
            value (float): value for IDD Field `value_until_time_140`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_140`'.format(value))

        self._data["Value Until Time 140"] = value

    @property
    def time_141(self):
        """Get time_141

        Returns:
            str: the value of `time_141` or None if not set
        """
        return self._data["Time 141"]

    @time_141.setter
    def time_141(self, value=None):
        """  Corresponds to IDD Field `time_141`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_141`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_141`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_141`')

        self._data["Time 141"] = value

    @property
    def value_until_time_141(self):
        """Get value_until_time_141

        Returns:
            float: the value of `value_until_time_141` or None if not set
        """
        return self._data["Value Until Time 141"]

    @value_until_time_141.setter
    def value_until_time_141(self, value=None):
        """  Corresponds to IDD Field `value_until_time_141`

        Args:
            value (float): value for IDD Field `value_until_time_141`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_141`'.format(value))

        self._data["Value Until Time 141"] = value

    @property
    def time_142(self):
        """Get time_142

        Returns:
            str: the value of `time_142` or None if not set
        """
        return self._data["Time 142"]

    @time_142.setter
    def time_142(self, value=None):
        """  Corresponds to IDD Field `time_142`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_142`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_142`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_142`')

        self._data["Time 142"] = value

    @property
    def value_until_time_142(self):
        """Get value_until_time_142

        Returns:
            float: the value of `value_until_time_142` or None if not set
        """
        return self._data["Value Until Time 142"]

    @value_until_time_142.setter
    def value_until_time_142(self, value=None):
        """  Corresponds to IDD Field `value_until_time_142`

        Args:
            value (float): value for IDD Field `value_until_time_142`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_142`'.format(value))

        self._data["Value Until Time 142"] = value

    @property
    def time_143(self):
        """Get time_143

        Returns:
            str: the value of `time_143` or None if not set
        """
        return self._data["Time 143"]

    @time_143.setter
    def time_143(self, value=None):
        """  Corresponds to IDD Field `time_143`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_143`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_143`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_143`')

        self._data["Time 143"] = value

    @property
    def value_until_time_143(self):
        """Get value_until_time_143

        Returns:
            float: the value of `value_until_time_143` or None if not set
        """
        return self._data["Value Until Time 143"]

    @value_until_time_143.setter
    def value_until_time_143(self, value=None):
        """  Corresponds to IDD Field `value_until_time_143`

        Args:
            value (float): value for IDD Field `value_until_time_143`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_143`'.format(value))

        self._data["Value Until Time 143"] = value

    @property
    def time_144(self):
        """Get time_144

        Returns:
            str: the value of `time_144` or None if not set
        """
        return self._data["Time 144"]

    @time_144.setter
    def time_144(self, value=None):
        """  Corresponds to IDD Field `time_144`
        "until" includes the time entered.

        Args:
            value (str): value for IDD Field `time_144`
                Unit: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_144`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_144`')

        self._data["Time 144"] = value

    @property
    def value_until_time_144(self):
        """Get value_until_time_144

        Returns:
            float: the value of `value_until_time_144` or None if not set
        """
        return self._data["Value Until Time 144"]

    @value_until_time_144.setter
    def value_until_time_144(self, value=None):
        """  Corresponds to IDD Field `value_until_time_144`

        Args:
            value (float): value for IDD Field `value_until_time_144`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `value_until_time_144`'.format(value))

        self._data["Value Until Time 144"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_type_limits_name))
        out.append(self._to_str(self.interpolate_to_timestep))
        out.append(self._to_str(self.time_1))
        out.append(self._to_str(self.value_until_time_1))
        out.append(self._to_str(self.time_2))
        out.append(self._to_str(self.value_until_time_2))
        out.append(self._to_str(self.time_3))
        out.append(self._to_str(self.value_until_time_3))
        out.append(self._to_str(self.time_4))
        out.append(self._to_str(self.value_until_time_4))
        out.append(self._to_str(self.time_5))
        out.append(self._to_str(self.value_until_time_5))
        out.append(self._to_str(self.time_6))
        out.append(self._to_str(self.value_until_time_6))
        out.append(self._to_str(self.time_7))
        out.append(self._to_str(self.value_until_time_7))
        out.append(self._to_str(self.time_8))
        out.append(self._to_str(self.value_until_time_8))
        out.append(self._to_str(self.time_9))
        out.append(self._to_str(self.value_until_time_9))
        out.append(self._to_str(self.time_10))
        out.append(self._to_str(self.value_until_time_10))
        out.append(self._to_str(self.time_11))
        out.append(self._to_str(self.value_until_time_11))
        out.append(self._to_str(self.time_12))
        out.append(self._to_str(self.value_until_time_12))
        out.append(self._to_str(self.time_13))
        out.append(self._to_str(self.value_until_time_13))
        out.append(self._to_str(self.time_14))
        out.append(self._to_str(self.value_until_time_14))
        out.append(self._to_str(self.time_15))
        out.append(self._to_str(self.value_until_time_15))
        out.append(self._to_str(self.time_16))
        out.append(self._to_str(self.value_until_time_16))
        out.append(self._to_str(self.time_17))
        out.append(self._to_str(self.value_until_time_17))
        out.append(self._to_str(self.time_18))
        out.append(self._to_str(self.value_until_time_18))
        out.append(self._to_str(self.time_19))
        out.append(self._to_str(self.value_until_time_19))
        out.append(self._to_str(self.time_20))
        out.append(self._to_str(self.value_until_time_20))
        out.append(self._to_str(self.time_21))
        out.append(self._to_str(self.value_until_time_21))
        out.append(self._to_str(self.time_22))
        out.append(self._to_str(self.value_until_time_22))
        out.append(self._to_str(self.time_23))
        out.append(self._to_str(self.value_until_time_23))
        out.append(self._to_str(self.time_24))
        out.append(self._to_str(self.value_until_time_24))
        out.append(self._to_str(self.time_25))
        out.append(self._to_str(self.value_until_time_25))
        out.append(self._to_str(self.time_26))
        out.append(self._to_str(self.value_until_time_26))
        out.append(self._to_str(self.time_27))
        out.append(self._to_str(self.value_until_time_27))
        out.append(self._to_str(self.time_28))
        out.append(self._to_str(self.value_until_time_28))
        out.append(self._to_str(self.time_29))
        out.append(self._to_str(self.value_until_time_29))
        out.append(self._to_str(self.time_30))
        out.append(self._to_str(self.value_until_time_30))
        out.append(self._to_str(self.time_31))
        out.append(self._to_str(self.value_until_time_31))
        out.append(self._to_str(self.time_32))
        out.append(self._to_str(self.value_until_time_32))
        out.append(self._to_str(self.time_33))
        out.append(self._to_str(self.value_until_time_33))
        out.append(self._to_str(self.time_34))
        out.append(self._to_str(self.value_until_time_34))
        out.append(self._to_str(self.time_35))
        out.append(self._to_str(self.value_until_time_35))
        out.append(self._to_str(self.time_36))
        out.append(self._to_str(self.value_until_time_36))
        out.append(self._to_str(self.time_37))
        out.append(self._to_str(self.value_until_time_37))
        out.append(self._to_str(self.time_38))
        out.append(self._to_str(self.value_until_time_38))
        out.append(self._to_str(self.time_39))
        out.append(self._to_str(self.value_until_time_39))
        out.append(self._to_str(self.time_40))
        out.append(self._to_str(self.value_until_time_40))
        out.append(self._to_str(self.time_41))
        out.append(self._to_str(self.value_until_time_41))
        out.append(self._to_str(self.time_42))
        out.append(self._to_str(self.value_until_time_42))
        out.append(self._to_str(self.time_43))
        out.append(self._to_str(self.value_until_time_43))
        out.append(self._to_str(self.time_44))
        out.append(self._to_str(self.value_until_time_44))
        out.append(self._to_str(self.time_45))
        out.append(self._to_str(self.value_until_time_45))
        out.append(self._to_str(self.time_46))
        out.append(self._to_str(self.value_until_time_46))
        out.append(self._to_str(self.time_47))
        out.append(self._to_str(self.value_until_time_47))
        out.append(self._to_str(self.time_48))
        out.append(self._to_str(self.value_until_time_48))
        out.append(self._to_str(self.time_49))
        out.append(self._to_str(self.value_until_time_49))
        out.append(self._to_str(self.time_50))
        out.append(self._to_str(self.value_until_time_50))
        out.append(self._to_str(self.time_51))
        out.append(self._to_str(self.value_until_time_51))
        out.append(self._to_str(self.time_52))
        out.append(self._to_str(self.value_until_time_52))
        out.append(self._to_str(self.time_53))
        out.append(self._to_str(self.value_until_time_53))
        out.append(self._to_str(self.time_54))
        out.append(self._to_str(self.value_until_time_54))
        out.append(self._to_str(self.time_55))
        out.append(self._to_str(self.value_until_time_55))
        out.append(self._to_str(self.time_56))
        out.append(self._to_str(self.value_until_time_56))
        out.append(self._to_str(self.time_57))
        out.append(self._to_str(self.value_until_time_57))
        out.append(self._to_str(self.time_58))
        out.append(self._to_str(self.value_until_time_58))
        out.append(self._to_str(self.time_59))
        out.append(self._to_str(self.value_until_time_59))
        out.append(self._to_str(self.time_60))
        out.append(self._to_str(self.value_until_time_60))
        out.append(self._to_str(self.time_61))
        out.append(self._to_str(self.value_until_time_61))
        out.append(self._to_str(self.time_62))
        out.append(self._to_str(self.value_until_time_62))
        out.append(self._to_str(self.time_63))
        out.append(self._to_str(self.value_until_time_63))
        out.append(self._to_str(self.time_64))
        out.append(self._to_str(self.value_until_time_64))
        out.append(self._to_str(self.time_65))
        out.append(self._to_str(self.value_until_time_65))
        out.append(self._to_str(self.time_66))
        out.append(self._to_str(self.value_until_time_66))
        out.append(self._to_str(self.time_67))
        out.append(self._to_str(self.value_until_time_67))
        out.append(self._to_str(self.time_68))
        out.append(self._to_str(self.value_until_time_68))
        out.append(self._to_str(self.time_69))
        out.append(self._to_str(self.value_until_time_69))
        out.append(self._to_str(self.time_70))
        out.append(self._to_str(self.value_until_time_70))
        out.append(self._to_str(self.time_71))
        out.append(self._to_str(self.value_until_time_71))
        out.append(self._to_str(self.time_72))
        out.append(self._to_str(self.value_until_time_72))
        out.append(self._to_str(self.time_73))
        out.append(self._to_str(self.value_until_time_73))
        out.append(self._to_str(self.time_74))
        out.append(self._to_str(self.value_until_time_74))
        out.append(self._to_str(self.time_75))
        out.append(self._to_str(self.value_until_time_75))
        out.append(self._to_str(self.time_76))
        out.append(self._to_str(self.value_until_time_76))
        out.append(self._to_str(self.time_77))
        out.append(self._to_str(self.value_until_time_77))
        out.append(self._to_str(self.time_78))
        out.append(self._to_str(self.value_until_time_78))
        out.append(self._to_str(self.time_79))
        out.append(self._to_str(self.value_until_time_79))
        out.append(self._to_str(self.time_80))
        out.append(self._to_str(self.value_until_time_80))
        out.append(self._to_str(self.time_81))
        out.append(self._to_str(self.value_until_time_81))
        out.append(self._to_str(self.time_82))
        out.append(self._to_str(self.value_until_time_82))
        out.append(self._to_str(self.time_83))
        out.append(self._to_str(self.value_until_time_83))
        out.append(self._to_str(self.time_84))
        out.append(self._to_str(self.value_until_time_84))
        out.append(self._to_str(self.time_85))
        out.append(self._to_str(self.value_until_time_85))
        out.append(self._to_str(self.time_86))
        out.append(self._to_str(self.value_until_time_86))
        out.append(self._to_str(self.time_87))
        out.append(self._to_str(self.value_until_time_87))
        out.append(self._to_str(self.time_88))
        out.append(self._to_str(self.value_until_time_88))
        out.append(self._to_str(self.time_89))
        out.append(self._to_str(self.value_until_time_89))
        out.append(self._to_str(self.time_90))
        out.append(self._to_str(self.value_until_time_90))
        out.append(self._to_str(self.time_91))
        out.append(self._to_str(self.value_until_time_91))
        out.append(self._to_str(self.time_92))
        out.append(self._to_str(self.value_until_time_92))
        out.append(self._to_str(self.time_93))
        out.append(self._to_str(self.value_until_time_93))
        out.append(self._to_str(self.time_94))
        out.append(self._to_str(self.value_until_time_94))
        out.append(self._to_str(self.time_95))
        out.append(self._to_str(self.value_until_time_95))
        out.append(self._to_str(self.time_96))
        out.append(self._to_str(self.value_until_time_96))
        out.append(self._to_str(self.time_97))
        out.append(self._to_str(self.value_until_time_97))
        out.append(self._to_str(self.time_98))
        out.append(self._to_str(self.value_until_time_98))
        out.append(self._to_str(self.time_99))
        out.append(self._to_str(self.value_until_time_99))
        out.append(self._to_str(self.time_100))
        out.append(self._to_str(self.value_until_time_100))
        out.append(self._to_str(self.time_101))
        out.append(self._to_str(self.value_until_time_101))
        out.append(self._to_str(self.time_102))
        out.append(self._to_str(self.value_until_time_102))
        out.append(self._to_str(self.time_103))
        out.append(self._to_str(self.value_until_time_103))
        out.append(self._to_str(self.time_104))
        out.append(self._to_str(self.value_until_time_104))
        out.append(self._to_str(self.time_105))
        out.append(self._to_str(self.value_until_time_105))
        out.append(self._to_str(self.time_106))
        out.append(self._to_str(self.value_until_time_106))
        out.append(self._to_str(self.time_107))
        out.append(self._to_str(self.value_until_time_107))
        out.append(self._to_str(self.time_108))
        out.append(self._to_str(self.value_until_time_108))
        out.append(self._to_str(self.time_109))
        out.append(self._to_str(self.value_until_time_109))
        out.append(self._to_str(self.time_110))
        out.append(self._to_str(self.value_until_time_110))
        out.append(self._to_str(self.time_111))
        out.append(self._to_str(self.value_until_time_111))
        out.append(self._to_str(self.time_112))
        out.append(self._to_str(self.value_until_time_112))
        out.append(self._to_str(self.time_113))
        out.append(self._to_str(self.value_until_time_113))
        out.append(self._to_str(self.time_114))
        out.append(self._to_str(self.value_until_time_114))
        out.append(self._to_str(self.time_115))
        out.append(self._to_str(self.value_until_time_115))
        out.append(self._to_str(self.time_116))
        out.append(self._to_str(self.value_until_time_116))
        out.append(self._to_str(self.time_117))
        out.append(self._to_str(self.value_until_time_117))
        out.append(self._to_str(self.time_118))
        out.append(self._to_str(self.value_until_time_118))
        out.append(self._to_str(self.time_119))
        out.append(self._to_str(self.value_until_time_119))
        out.append(self._to_str(self.time_120))
        out.append(self._to_str(self.value_until_time_120))
        out.append(self._to_str(self.time_121))
        out.append(self._to_str(self.value_until_time_121))
        out.append(self._to_str(self.time_122))
        out.append(self._to_str(self.value_until_time_122))
        out.append(self._to_str(self.time_123))
        out.append(self._to_str(self.value_until_time_123))
        out.append(self._to_str(self.time_124))
        out.append(self._to_str(self.value_until_time_124))
        out.append(self._to_str(self.time_125))
        out.append(self._to_str(self.value_until_time_125))
        out.append(self._to_str(self.time_126))
        out.append(self._to_str(self.value_until_time_126))
        out.append(self._to_str(self.time_127))
        out.append(self._to_str(self.value_until_time_127))
        out.append(self._to_str(self.time_128))
        out.append(self._to_str(self.value_until_time_128))
        out.append(self._to_str(self.time_129))
        out.append(self._to_str(self.value_until_time_129))
        out.append(self._to_str(self.time_130))
        out.append(self._to_str(self.value_until_time_130))
        out.append(self._to_str(self.time_131))
        out.append(self._to_str(self.value_until_time_131))
        out.append(self._to_str(self.time_132))
        out.append(self._to_str(self.value_until_time_132))
        out.append(self._to_str(self.time_133))
        out.append(self._to_str(self.value_until_time_133))
        out.append(self._to_str(self.time_134))
        out.append(self._to_str(self.value_until_time_134))
        out.append(self._to_str(self.time_135))
        out.append(self._to_str(self.value_until_time_135))
        out.append(self._to_str(self.time_136))
        out.append(self._to_str(self.value_until_time_136))
        out.append(self._to_str(self.time_137))
        out.append(self._to_str(self.value_until_time_137))
        out.append(self._to_str(self.time_138))
        out.append(self._to_str(self.value_until_time_138))
        out.append(self._to_str(self.time_139))
        out.append(self._to_str(self.value_until_time_139))
        out.append(self._to_str(self.time_140))
        out.append(self._to_str(self.value_until_time_140))
        out.append(self._to_str(self.time_141))
        out.append(self._to_str(self.value_until_time_141))
        out.append(self._to_str(self.time_142))
        out.append(self._to_str(self.value_until_time_142))
        out.append(self._to_str(self.time_143))
        out.append(self._to_str(self.value_until_time_143))
        out.append(self._to_str(self.time_144))
        out.append(self._to_str(self.value_until_time_144))
        return ",".join(out)

class ScheduleWeekDaily(object):
    """ Corresponds to IDD object `Schedule:Week:Daily`
        A Schedule:Week:Daily contains 12 Schedule:Day:Hourly objects, one for each day type.
    """
    internal_name = "Schedule:Week:Daily"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Week:Daily`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Sunday Schedule:Day Name"] = None
        self._data["Monday Schedule:Day Name"] = None
        self._data["Tuesday Schedule:Day Name"] = None
        self._data["Wednesday Schedule:Day Name"] = None
        self._data["Thursday Schedule:Day Name"] = None
        self._data["Friday Schedule:Day Name"] = None
        self._data["Saturday Schedule:Day Name"] = None
        self._data["Holiday Schedule:Day Name"] = None
        self._data["SummerDesignDay Schedule:Day Name"] = None
        self._data["WinterDesignDay Schedule:Day Name"] = None
        self._data["CustomDay1 Schedule:Day Name"] = None
        self._data["CustomDay2 Schedule:Day Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sunday_scheduleday_name = None
        else:
            self.sunday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.monday_scheduleday_name = None
        else:
            self.monday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tuesday_scheduleday_name = None
        else:
            self.tuesday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wednesday_scheduleday_name = None
        else:
            self.wednesday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thursday_scheduleday_name = None
        else:
            self.thursday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.friday_scheduleday_name = None
        else:
            self.friday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.saturday_scheduleday_name = None
        else:
            self.saturday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.holiday_scheduleday_name = None
        else:
            self.holiday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.summerdesignday_scheduleday_name = None
        else:
            self.summerdesignday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.winterdesignday_scheduleday_name = None
        else:
            self.winterdesignday_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.customday1_scheduleday_name = None
        else:
            self.customday1_scheduleday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.customday2_scheduleday_name = None
        else:
            self.customday2_scheduleday_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def sunday_scheduleday_name(self):
        """Get sunday_scheduleday_name

        Returns:
            str: the value of `sunday_scheduleday_name` or None if not set
        """
        return self._data["Sunday Schedule:Day Name"]

    @sunday_scheduleday_name.setter
    def sunday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `sunday_scheduleday_name`

        Args:
            value (str): value for IDD Field `sunday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sunday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sunday_scheduleday_name`')

        self._data["Sunday Schedule:Day Name"] = value

    @property
    def monday_scheduleday_name(self):
        """Get monday_scheduleday_name

        Returns:
            str: the value of `monday_scheduleday_name` or None if not set
        """
        return self._data["Monday Schedule:Day Name"]

    @monday_scheduleday_name.setter
    def monday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `monday_scheduleday_name`

        Args:
            value (str): value for IDD Field `monday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `monday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `monday_scheduleday_name`')

        self._data["Monday Schedule:Day Name"] = value

    @property
    def tuesday_scheduleday_name(self):
        """Get tuesday_scheduleday_name

        Returns:
            str: the value of `tuesday_scheduleday_name` or None if not set
        """
        return self._data["Tuesday Schedule:Day Name"]

    @tuesday_scheduleday_name.setter
    def tuesday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `tuesday_scheduleday_name`

        Args:
            value (str): value for IDD Field `tuesday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tuesday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tuesday_scheduleday_name`')

        self._data["Tuesday Schedule:Day Name"] = value

    @property
    def wednesday_scheduleday_name(self):
        """Get wednesday_scheduleday_name

        Returns:
            str: the value of `wednesday_scheduleday_name` or None if not set
        """
        return self._data["Wednesday Schedule:Day Name"]

    @wednesday_scheduleday_name.setter
    def wednesday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `wednesday_scheduleday_name`

        Args:
            value (str): value for IDD Field `wednesday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wednesday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wednesday_scheduleday_name`')

        self._data["Wednesday Schedule:Day Name"] = value

    @property
    def thursday_scheduleday_name(self):
        """Get thursday_scheduleday_name

        Returns:
            str: the value of `thursday_scheduleday_name` or None if not set
        """
        return self._data["Thursday Schedule:Day Name"]

    @thursday_scheduleday_name.setter
    def thursday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `thursday_scheduleday_name`

        Args:
            value (str): value for IDD Field `thursday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thursday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thursday_scheduleday_name`')

        self._data["Thursday Schedule:Day Name"] = value

    @property
    def friday_scheduleday_name(self):
        """Get friday_scheduleday_name

        Returns:
            str: the value of `friday_scheduleday_name` or None if not set
        """
        return self._data["Friday Schedule:Day Name"]

    @friday_scheduleday_name.setter
    def friday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `friday_scheduleday_name`

        Args:
            value (str): value for IDD Field `friday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `friday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `friday_scheduleday_name`')

        self._data["Friday Schedule:Day Name"] = value

    @property
    def saturday_scheduleday_name(self):
        """Get saturday_scheduleday_name

        Returns:
            str: the value of `saturday_scheduleday_name` or None if not set
        """
        return self._data["Saturday Schedule:Day Name"]

    @saturday_scheduleday_name.setter
    def saturday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `saturday_scheduleday_name`

        Args:
            value (str): value for IDD Field `saturday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `saturday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `saturday_scheduleday_name`')

        self._data["Saturday Schedule:Day Name"] = value

    @property
    def holiday_scheduleday_name(self):
        """Get holiday_scheduleday_name

        Returns:
            str: the value of `holiday_scheduleday_name` or None if not set
        """
        return self._data["Holiday Schedule:Day Name"]

    @holiday_scheduleday_name.setter
    def holiday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `holiday_scheduleday_name`

        Args:
            value (str): value for IDD Field `holiday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `holiday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `holiday_scheduleday_name`')

        self._data["Holiday Schedule:Day Name"] = value

    @property
    def summerdesignday_scheduleday_name(self):
        """Get summerdesignday_scheduleday_name

        Returns:
            str: the value of `summerdesignday_scheduleday_name` or None if not set
        """
        return self._data["SummerDesignDay Schedule:Day Name"]

    @summerdesignday_scheduleday_name.setter
    def summerdesignday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `summerdesignday_scheduleday_name`

        Args:
            value (str): value for IDD Field `summerdesignday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `summerdesignday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `summerdesignday_scheduleday_name`')

        self._data["SummerDesignDay Schedule:Day Name"] = value

    @property
    def winterdesignday_scheduleday_name(self):
        """Get winterdesignday_scheduleday_name

        Returns:
            str: the value of `winterdesignday_scheduleday_name` or None if not set
        """
        return self._data["WinterDesignDay Schedule:Day Name"]

    @winterdesignday_scheduleday_name.setter
    def winterdesignday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `winterdesignday_scheduleday_name`

        Args:
            value (str): value for IDD Field `winterdesignday_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `winterdesignday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `winterdesignday_scheduleday_name`')

        self._data["WinterDesignDay Schedule:Day Name"] = value

    @property
    def customday1_scheduleday_name(self):
        """Get customday1_scheduleday_name

        Returns:
            str: the value of `customday1_scheduleday_name` or None if not set
        """
        return self._data["CustomDay1 Schedule:Day Name"]

    @customday1_scheduleday_name.setter
    def customday1_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `customday1_scheduleday_name`

        Args:
            value (str): value for IDD Field `customday1_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `customday1_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `customday1_scheduleday_name`')

        self._data["CustomDay1 Schedule:Day Name"] = value

    @property
    def customday2_scheduleday_name(self):
        """Get customday2_scheduleday_name

        Returns:
            str: the value of `customday2_scheduleday_name` or None if not set
        """
        return self._data["CustomDay2 Schedule:Day Name"]

    @customday2_scheduleday_name.setter
    def customday2_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `customday2_scheduleday_name`

        Args:
            value (str): value for IDD Field `customday2_scheduleday_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `customday2_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `customday2_scheduleday_name`')

        self._data["CustomDay2 Schedule:Day Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.sunday_scheduleday_name))
        out.append(self._to_str(self.monday_scheduleday_name))
        out.append(self._to_str(self.tuesday_scheduleday_name))
        out.append(self._to_str(self.wednesday_scheduleday_name))
        out.append(self._to_str(self.thursday_scheduleday_name))
        out.append(self._to_str(self.friday_scheduleday_name))
        out.append(self._to_str(self.saturday_scheduleday_name))
        out.append(self._to_str(self.holiday_scheduleday_name))
        out.append(self._to_str(self.summerdesignday_scheduleday_name))
        out.append(self._to_str(self.winterdesignday_scheduleday_name))
        out.append(self._to_str(self.customday1_scheduleday_name))
        out.append(self._to_str(self.customday2_scheduleday_name))
        return ",".join(out)

class ScheduleWeekCompact(object):
    """ Corresponds to IDD object `Schedule:Week:Compact`
        Compact definition for Schedule:Day:List
    """
    internal_name = "Schedule:Week:Compact"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Week:Compact`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["DayType List 1"] = None
        self._data["Schedule:Day Name 1"] = None
        self._data["DayType List 2"] = None
        self._data["Schedule:Day Name 2"] = None
        self._data["DayType List 3"] = None
        self._data["Schedule:Day Name 3"] = None
        self._data["DayType List 4"] = None
        self._data["Schedule:Day Name 4"] = None
        self._data["DayType List 5"] = None
        self._data["Schedule:Day Name 5"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daytype_list_1 = None
        else:
            self.daytype_list_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.scheduleday_name_1 = None
        else:
            self.scheduleday_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daytype_list_2 = None
        else:
            self.daytype_list_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.scheduleday_name_2 = None
        else:
            self.scheduleday_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daytype_list_3 = None
        else:
            self.daytype_list_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.scheduleday_name_3 = None
        else:
            self.scheduleday_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daytype_list_4 = None
        else:
            self.daytype_list_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.scheduleday_name_4 = None
        else:
            self.scheduleday_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daytype_list_5 = None
        else:
            self.daytype_list_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.scheduleday_name_5 = None
        else:
            self.scheduleday_name_5 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def daytype_list_1(self):
        """Get daytype_list_1

        Returns:
            str: the value of `daytype_list_1` or None if not set
        """
        return self._data["DayType List 1"]

    @daytype_list_1.setter
    def daytype_list_1(self, value=None):
        """  Corresponds to IDD Field `daytype_list_1`
        "For" is an optional prefix/start of the For fields.  Choices can be combined on single line
        if separated by spaces. i.e. "Holiday Weekends"
        Should have a space after For, if it is included. i.e. "For Alldays"

        Args:
            value (str): value for IDD Field `daytype_list_1`
                Accepted values are:
                      - AllDays
                      - Weekdays
                      - Weekends
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `daytype_list_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daytype_list_1`')
            vals = set()
            vals.add("AllDays")
            vals.add("Weekdays")
            vals.add("Weekends")
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daytype_list_1`'.format(value))

        self._data["DayType List 1"] = value

    @property
    def scheduleday_name_1(self):
        """Get scheduleday_name_1

        Returns:
            str: the value of `scheduleday_name_1` or None if not set
        """
        return self._data["Schedule:Day Name 1"]

    @scheduleday_name_1.setter
    def scheduleday_name_1(self, value=None):
        """  Corresponds to IDD Field `scheduleday_name_1`

        Args:
            value (str): value for IDD Field `scheduleday_name_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `scheduleday_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `scheduleday_name_1`')

        self._data["Schedule:Day Name 1"] = value

    @property
    def daytype_list_2(self):
        """Get daytype_list_2

        Returns:
            str: the value of `daytype_list_2` or None if not set
        """
        return self._data["DayType List 2"]

    @daytype_list_2.setter
    def daytype_list_2(self, value=None):
        """  Corresponds to IDD Field `daytype_list_2`

        Args:
            value (str): value for IDD Field `daytype_list_2`
                Accepted values are:
                      - AllOtherDays
                      - Weekdays
                      - Weekends
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `daytype_list_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daytype_list_2`')
            vals = set()
            vals.add("AllOtherDays")
            vals.add("Weekdays")
            vals.add("Weekends")
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daytype_list_2`'.format(value))

        self._data["DayType List 2"] = value

    @property
    def scheduleday_name_2(self):
        """Get scheduleday_name_2

        Returns:
            str: the value of `scheduleday_name_2` or None if not set
        """
        return self._data["Schedule:Day Name 2"]

    @scheduleday_name_2.setter
    def scheduleday_name_2(self, value=None):
        """  Corresponds to IDD Field `scheduleday_name_2`

        Args:
            value (str): value for IDD Field `scheduleday_name_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `scheduleday_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `scheduleday_name_2`')

        self._data["Schedule:Day Name 2"] = value

    @property
    def daytype_list_3(self):
        """Get daytype_list_3

        Returns:
            str: the value of `daytype_list_3` or None if not set
        """
        return self._data["DayType List 3"]

    @daytype_list_3.setter
    def daytype_list_3(self, value=None):
        """  Corresponds to IDD Field `daytype_list_3`

        Args:
            value (str): value for IDD Field `daytype_list_3`
                Accepted values are:
                      - AllOtherDays
                      - Weekdays
                      - Weekends
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `daytype_list_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daytype_list_3`')
            vals = set()
            vals.add("AllOtherDays")
            vals.add("Weekdays")
            vals.add("Weekends")
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daytype_list_3`'.format(value))

        self._data["DayType List 3"] = value

    @property
    def scheduleday_name_3(self):
        """Get scheduleday_name_3

        Returns:
            str: the value of `scheduleday_name_3` or None if not set
        """
        return self._data["Schedule:Day Name 3"]

    @scheduleday_name_3.setter
    def scheduleday_name_3(self, value=None):
        """  Corresponds to IDD Field `scheduleday_name_3`

        Args:
            value (str): value for IDD Field `scheduleday_name_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `scheduleday_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `scheduleday_name_3`')

        self._data["Schedule:Day Name 3"] = value

    @property
    def daytype_list_4(self):
        """Get daytype_list_4

        Returns:
            str: the value of `daytype_list_4` or None if not set
        """
        return self._data["DayType List 4"]

    @daytype_list_4.setter
    def daytype_list_4(self, value=None):
        """  Corresponds to IDD Field `daytype_list_4`

        Args:
            value (str): value for IDD Field `daytype_list_4`
                Accepted values are:
                      - AllOtherDays
                      - Weekdays
                      - Weekends
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `daytype_list_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daytype_list_4`')
            vals = set()
            vals.add("AllOtherDays")
            vals.add("Weekdays")
            vals.add("Weekends")
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daytype_list_4`'.format(value))

        self._data["DayType List 4"] = value

    @property
    def scheduleday_name_4(self):
        """Get scheduleday_name_4

        Returns:
            str: the value of `scheduleday_name_4` or None if not set
        """
        return self._data["Schedule:Day Name 4"]

    @scheduleday_name_4.setter
    def scheduleday_name_4(self, value=None):
        """  Corresponds to IDD Field `scheduleday_name_4`

        Args:
            value (str): value for IDD Field `scheduleday_name_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `scheduleday_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `scheduleday_name_4`')

        self._data["Schedule:Day Name 4"] = value

    @property
    def daytype_list_5(self):
        """Get daytype_list_5

        Returns:
            str: the value of `daytype_list_5` or None if not set
        """
        return self._data["DayType List 5"]

    @daytype_list_5.setter
    def daytype_list_5(self, value=None):
        """  Corresponds to IDD Field `daytype_list_5`

        Args:
            value (str): value for IDD Field `daytype_list_5`
                Accepted values are:
                      - AllOtherDays
                      - Weekdays
                      - Weekends
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `daytype_list_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daytype_list_5`')
            vals = set()
            vals.add("AllOtherDays")
            vals.add("Weekdays")
            vals.add("Weekends")
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daytype_list_5`'.format(value))

        self._data["DayType List 5"] = value

    @property
    def scheduleday_name_5(self):
        """Get scheduleday_name_5

        Returns:
            str: the value of `scheduleday_name_5` or None if not set
        """
        return self._data["Schedule:Day Name 5"]

    @scheduleday_name_5.setter
    def scheduleday_name_5(self, value=None):
        """  Corresponds to IDD Field `scheduleday_name_5`

        Args:
            value (str): value for IDD Field `scheduleday_name_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `scheduleday_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `scheduleday_name_5`')

        self._data["Schedule:Day Name 5"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.daytype_list_1))
        out.append(self._to_str(self.scheduleday_name_1))
        out.append(self._to_str(self.daytype_list_2))
        out.append(self._to_str(self.scheduleday_name_2))
        out.append(self._to_str(self.daytype_list_3))
        out.append(self._to_str(self.scheduleday_name_3))
        out.append(self._to_str(self.daytype_list_4))
        out.append(self._to_str(self.scheduleday_name_4))
        out.append(self._to_str(self.daytype_list_5))
        out.append(self._to_str(self.scheduleday_name_5))
        return ",".join(out)

class ScheduleConstant(object):
    """ Corresponds to IDD object `Schedule:Constant`
        Constant hourly value for entire year.
    """
    internal_name = "Schedule:Constant"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Constant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Hourly Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hourly_value = None
        else:
            self.hourly_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_name`

        Args:
            value (str): value for IDD Field `schedule_type_limits_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_name`')

        self._data["Schedule Type Limits Name"] = value

    @property
    def hourly_value(self):
        """Get hourly_value

        Returns:
            float: the value of `hourly_value` or None if not set
        """
        return self._data["Hourly Value"]

    @hourly_value.setter
    def hourly_value(self, value=0.0 ):
        """  Corresponds to IDD Field `hourly_value`

        Args:
            value (float): value for IDD Field `hourly_value`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hourly_value`'.format(value))

        self._data["Hourly Value"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_type_limits_name))
        out.append(self._to_str(self.hourly_value))
        return ",".join(out)

class ScheduleFile(object):
    """ Corresponds to IDD object `Schedule:File`
        A Schedule:File points to a text computer file that has 8760-8784 hours of data.
    """
    internal_name = "Schedule:File"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:File`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["File Name"] = None
        self._data["Column Number"] = None
        self._data["Rows to Skip at Top"] = None
        self._data["Number of Hours of Data"] = None
        self._data["Column Separator"] = None
        self._data["Interpolate to Timestep"] = None
        self._data["Minutes per Item"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.file_name = None
        else:
            self.file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.column_number = None
        else:
            self.column_number = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rows_to_skip_at_top = None
        else:
            self.rows_to_skip_at_top = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_hours_of_data = None
        else:
            self.number_of_hours_of_data = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.interpolate_to_timestep = None
        else:
            self.interpolate_to_timestep = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minutes_per_item = None
        else:
            self.minutes_per_item = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_name`

        Args:
            value (str): value for IDD Field `schedule_type_limits_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_name`')

        self._data["Schedule Type Limits Name"] = value

    @property
    def file_name(self):
        """Get file_name

        Returns:
            str: the value of `file_name` or None if not set
        """
        return self._data["File Name"]

    @file_name.setter
    def file_name(self, value=None):
        """  Corresponds to IDD Field `file_name`

        Args:
            value (str): value for IDD Field `file_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `file_name`')

        self._data["File Name"] = value

    @property
    def column_number(self):
        """Get column_number

        Returns:
            int: the value of `column_number` or None if not set
        """
        return self._data["Column Number"]

    @column_number.setter
    def column_number(self, value=None):
        """  Corresponds to IDD Field `column_number`

        Args:
            value (int): value for IDD Field `column_number`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `column_number`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `column_number`')

        self._data["Column Number"] = value

    @property
    def rows_to_skip_at_top(self):
        """Get rows_to_skip_at_top

        Returns:
            int: the value of `rows_to_skip_at_top` or None if not set
        """
        return self._data["Rows to Skip at Top"]

    @rows_to_skip_at_top.setter
    def rows_to_skip_at_top(self, value=None):
        """  Corresponds to IDD Field `rows_to_skip_at_top`

        Args:
            value (int): value for IDD Field `rows_to_skip_at_top`
                value >= 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `rows_to_skip_at_top`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rows_to_skip_at_top`')

        self._data["Rows to Skip at Top"] = value

    @property
    def number_of_hours_of_data(self):
        """Get number_of_hours_of_data

        Returns:
            float: the value of `number_of_hours_of_data` or None if not set
        """
        return self._data["Number of Hours of Data"]

    @number_of_hours_of_data.setter
    def number_of_hours_of_data(self, value=8760.0 ):
        """  Corresponds to IDD Field `number_of_hours_of_data`
        8760 hours does not account for leap years, 8784 does.
        should be either 8760 or 8784

        Args:
            value (float): value for IDD Field `number_of_hours_of_data`
                Default value: 8760.0
                value >= 8760.0
                value <= 8784.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_hours_of_data`'.format(value))
            if value < 8760.0:
                raise ValueError('value need to be greater or equal 8760.0 '
                                 'for field `number_of_hours_of_data`')
            if value > 8784.0:
                raise ValueError('value need to be smaller 8784.0 '
                                 'for field `number_of_hours_of_data`')

        self._data["Number of Hours of Data"] = value

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `column_separator`

        Args:
            value (str): value for IDD Field `column_separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                      - Semicolon
                Default value: Comma
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `column_separator`')
            vals = set()
            vals.add("Comma")
            vals.add("Tab")
            vals.add("Fixed")
            vals.add("Semicolon")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `column_separator`'.format(value))

        self._data["Column Separator"] = value

    @property
    def interpolate_to_timestep(self):
        """Get interpolate_to_timestep

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set
        """
        return self._data["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """  Corresponds to IDD Field `interpolate_to_timestep`
        when the interval does not match the user specified timestep a "Yes" choice will average between the intervals request (to
        timestep resolution.  a "No" choice will use the interval value at the simulation timestep without regard to if it matches
        the boundary or not.

        Args:
            value (str): value for IDD Field `interpolate_to_timestep`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `interpolate_to_timestep`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `interpolate_to_timestep`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `interpolate_to_timestep`'.format(value))

        self._data["Interpolate to Timestep"] = value

    @property
    def minutes_per_item(self):
        """Get minutes_per_item

        Returns:
            int: the value of `minutes_per_item` or None if not set
        """
        return self._data["Minutes per Item"]

    @minutes_per_item.setter
    def minutes_per_item(self, value=None):
        """  Corresponds to IDD Field `minutes_per_item`
        Must be evenly divisible into 60

        Args:
            value (int): value for IDD Field `minutes_per_item`
                value >= 1
                value <= 60
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `minutes_per_item`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `minutes_per_item`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `minutes_per_item`')

        self._data["Minutes per Item"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_type_limits_name))
        out.append(self._to_str(self.file_name))
        out.append(self._to_str(self.column_number))
        out.append(self._to_str(self.rows_to_skip_at_top))
        out.append(self._to_str(self.number_of_hours_of_data))
        out.append(self._to_str(self.column_separator))
        out.append(self._to_str(self.interpolate_to_timestep))
        out.append(self._to_str(self.minutes_per_item))
        return ",".join(out)