"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from turtle import distance
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object,
    such as its primary designation (required, unique), IAU name, diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        :self.designation: initializes designation
        :self.name: initializes name
        :dia: diameteter of object
        :self.diameter: initializes diameteter of object as float
        :self.hazardous: initializes hazardous
        """
        self.designation = info.get("designation")
        self.name = info.get("name", None)
        dia = info["diameter"] if info["diameter"] else 'nan'
        self.diameter = float(dia)
        self.hazardous = info["hazardous"] == 'Y'

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return self.designation + " " + self.name
        return "{}".format(self.designation)

    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous:
            return f"NEO 2020 FK {self.name} has a diameter of " \
                f"{self.diameter} and is potentially hazardous."
        return f"NEO 2020 FK {self.name} has diameter of {self.diameter} " \
            "and is not hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r} ," \
            f"name={self.name!r}, " \
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"
    
    def serial(self):
        """Return a dict representation of self attributes.

        Returns: Keys associated with self attributes.
        """
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }



class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
    to Earth, such as the date and time (in UTC) of closest approach,
    the nominal approach distance in astronomical units, and the relative
    approach velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        """
        self._designation = info.get('des')
        self.time = cd_to_datetime(info.get('cd'))
        dist = info.get('dist', 'nan')
        vel = info.get('v_rel', 'nan')
        self.distance = float(dist)
        self.velocity = float(vel)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = info.get("neo")

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't
        exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        tm = datetime_to_str(self.time)
        return tm

    def __str__(self):
        """Return `str(self)`."""
        return f"On {self.time_str}; '{self.neo.fullname}' approaches the " \
            f"Earth with a velocity of and a distance of {self.velocity:.2f}" \
            f" au and a velocity of {self.distance:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, " \
            f"distance={self.distance:.2f}, " \
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
    
    def serial(self):
        """Return a dict representation of self attributes.
        
        Returns:
            [dict]: Keys associated with self attributes.
            
        """
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
        }
