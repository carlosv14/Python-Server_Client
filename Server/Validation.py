import re
class Validation:

    @staticmethod
    def validEmail(email):
        if re.match('(\w+(.)+@\w+(?:\.\w+)+)',email):
            return 1
        return 0

    @staticmethod
    def validDate(Date):
        if re.match('(\d{2}[-/]\d{2}[-/]\d{4})',Date):
            return 1
        return 0

    @staticmethod
    def validID(ID):
        if re.match('(\d{4}\-\d{4}\-\d{5})',ID):
            return 1
        return 0

    @staticmethod
    def Unique(users,param, paramtype):
        for u in users:
            if paramtype == 0:
                if u.username == param:
                    return 0
            elif paramtype == 1:
                if u.email == param:
                    return 0
            elif paramtype == 2:
                if u.id == param:
                    return 0
        return 1




