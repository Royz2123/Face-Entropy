import numpy as np


import constants
import face_transform as f_t
import util

class Face(object):
    def __init__(self, filename="", features=[]):
        if filename != "":
            self._filename = filename
        else:
            self._filename = constants.GENERATED_FACE_FILENAME
        self._features = features

    def distance(self, other):
        return np.linalg.norm(self._features - other._features)

    def __eq__(self, other):
        return self.distance(other) < constants.MIN_DISTANCE

    def __repr__(self):
        return """
        Name:\t\t%s\n
        Feature Vector:\t%s\n
        """ % (
            self._filename,
            self._features
        )

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, f):
        self._features = f

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, f):
        self._filename = f

    def set_features(self, face_transform):
        # read the image
        face_im = util.read_image(self._filename)

        # find features
        features = face_transform.find_features(face_im)

        if features is None:
            return -1

        self._features = features
        return 0
