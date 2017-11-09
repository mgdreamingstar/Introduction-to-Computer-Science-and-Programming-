# Author: guorch@buaa.edu.cn
# doubly_linked_list.py
# 2017/11/9 21:42 

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before

    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name

def insert(atMe, newFrob):
    '''
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    '''
    item = atMe
    # print item.before.name
    while item.before != None:
        item = item.before

    while item.after != None:
        if newFrob.name[0] < item.name[0]:
            temp = item.getBefore()
            item.setBefore(newFrob)
            temp.setAfter(newFrob)
            newFrob.setBefore(temp)
            newFrob.setAfter(item)
        item = item.after
    else:
        if newFrob.name[0] > item.name[0]:
            newFrob.setBefore(item)
            item.setAfter(newFrob)
        else:
            if item.getBefore() != None:
                temp = item.getBefore()
                newFrob.setAfter(item)
                item.setBefore(newFrob)

                temp.setAfter(newFrob)
                newFrob.setBefore(temp)
            else:
                newFrob.setAfter(item)
                item.setBefore(newFrob)


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
try:
    print 'before', eric.before.name
except:
    print 'after', eric.after.name
insert(eric, ruth)
print 'after', eric.after.name
insert(eric, fred)
print 'after', eric.after.name
insert(ruth, martha)

print ruth.getBefore().name
