class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif len(new_name) < 3:
            raise ValueError("Name must be more than 3 characters")
        elif hasattr(self, "name"):
            raise TypeError("National Park name cannot be changed")
        else:
            self._name = new_name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        connesieur = None
        most_visits = 0
        current_visits = 0
        for person in Visitor.all:
            for trip in self.trips():
                if trip.visitor == person:
                    current_visits += 1
            if current_visits > most_visits:
                most_visits = current_visits
                connesieur = person
            current_visits = 0
        return connesieur
    
    @classmethod
    def most_visited(cls):
        most_visits = 0
        best_park = None
        for park in cls.all:
            visits = len(park.trips())
            if visits > most_visits:
                best_park = park
                most_visits = visits
        return best_park

class Trip:
    all = []
    MONTHS = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, new_visitor):
        if not isinstance(new_visitor, Visitor):
            raise TypeError("Visitor must be of Visitor class")
        else:
            self._visitor = new_visitor
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, new_park):
        if not isinstance(new_park, NationalPark):
            raise TypeError("Park must be of National Park class")
        else:
            self._national_park = new_park

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, new_start_date):
        parts = new_start_date.split()
        if not isinstance(new_start_date, str):
            raise TypeError("Start Date must be a string")
        elif len(new_start_date) < 7:
            raise ValueError("Start Date must be more than 7 characters")
        elif not len(parts) == 2 and not parts[0] in type(self).MONTHS:
            raise ValueError("Date must be in format 'September 1st'")
        else:
            self._start_date = new_start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, new_end_date):
        parts = new_end_date.split()
        if not isinstance(new_end_date, str):
            raise TypeError("End Date must be a string")
        elif len(new_end_date) < 7:
            raise ValueError("End Date must be more than 7 characters")
        elif not len(parts) == 2 and not parts[0] in type(self).MONTHS:
            raise ValueError("Date must be in format 'September 1st'")
        else:
            self._end_date = new_end_date

class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif not 0 < len(new_name) < 16:
            raise ValueError("Name must be between 1-15 characters")
        else:
            self._name = new_name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        return len([trip for trip in Trip.all if trip.national_park is park])