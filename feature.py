
class Feature(object):
    def __init__(self, version):
        self.version = version
        self.id = None

    def set_id(self, id):
        print("Setting ID v2 for version {}".format(self.version))
        self.id = id

    def get_id(self):
        print("Getting ID v2 for version {}".format(self.version))
        return self.id


def get_feature(version):
    return Feature(version)
