import csv


class Subject:
    def __init__(self, demographics):
        self.id = int(demographics["id"])
        self.gender = demographics["gender"]
        self.age_range = demographics["age"]
        if demographics["forrest_seen_count"]:
            self.forrest_seen_count = int(demographics["forrest_seen_count"])
        # Accounting for case of missing data
        else:
            self.forrest_seen_count = -1


def parse_csv(fname):
    """
	Parses the given demographics.csv file and creates instances for each
    subject. Returns subject instances in a list.

	Parameters
	----------
	fname : string

	Returns 
	-------
	subjects : array
	"""
    subjects = []
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subjects.append(Subject(row))
        return subjects


def seen_most_times(subjects):
    """
    Identifies which subject has seen Forrest Gump the most times. Ties are
    broken arbitrarily. If no one has seen Forrest Gump before, returned
    subject ID will be -1.

    Parameters
    ---------
    subjects : array

    Returns
    -------
    subject : tuple
    Tuple contains both the count of how many times watched and subject's ID
    """
    count = 0
    subject_id = -1
    for subject in subjects:
        if subject.forrest_seen_count > count:
            count = subject.forrest_seen_count
            subject_id = subject.id
    return (count, subject_id)


def seen_least_times(subjects):
    """
    Identifies which subject has seen Forrest Gump the least times. Ties are
    broken arbitrarily.

    Parameters
    ----------
    subjects : array

    Returns
    -------
    subject : tuple
    Tuple contains both the count of how many times watched and subject's ID
    """
    count = 1000
    subject_id = -1
    for subject in subjects:
        subject.forrest_seen_count = curr_count
        if curr_count < count and curr_count > -1:
            count = curr_count
            subject_id = subject.id
    return (count, subject_id)


def find_id_by_gender(subjects, gender):
    """
    Identifies the ID's of a given gender

    Parameters
    ----------
    subjects : array
    gender : string

    Returns 
    -------
    ids : int array
    """
    ids = []
    for subject in subjects:
        if subject.gender == gender:
            ids.append(subject.id)
    return ids


def find_count_by_id(subjects, sid):
    """
    Finds the number of times a particular subject has seen Forrest Gump given
    his or her ID.

    Parameters
    ----------
    subjects : array
    sid : int

    Returns
    -------
    forrest_seen_count : int
    """
    for subject in subjects:
        if subject.id == sid:
            return subject.forrest_seen_count
