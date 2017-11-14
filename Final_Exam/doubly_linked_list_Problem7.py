# Author: guorch@buaa.edu.cn
# doubly_linked_list_Problem7.py
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
    # First two Frobs
    if atMe.getBefore() == None and atMe.getAfter() == None:
        if atMe.name[0] <= newFrob.name[0]:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            return
        else:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            return

    # put pointer at beginning
    pointer = atMe
    while pointer.before != None:
        pointer = pointer.before

    # search from start to end
    while pointer.after != None:

        # insert at beginning
        if newFrob.name[0] <= pointer.name[0] and pointer.getBefore() == None:
            pointer.setBefore(newFrob)
            newFrob.setAfter(pointer)
            return # end this
        # insert at middle
        # find the one after newFrob
        elif newFrob.name[0] <= pointer.name[0]:   # if newFrob <= pointer, insert before it.
            temp = pointer.getBefore()
            pointer.setBefore(newFrob)
            temp.setAfter(newFrob)
            newFrob.setBefore(temp)
            newFrob.setAfter(pointer)
            return # end this
        # move to next Frob
        pointer = pointer.getAfter() # pointer = start + 1

    else: # insert at the end, pointer = end
        if pointer.name[0] <= newFrob.name[0]:
            newFrob.setBefore(pointer)
            pointer.setAfter(newFrob)
        else:
            temp = pointer.getBefore()
            newFrob.setAfter(pointer)
            pointer.setBefore(newFrob)

            temp.setAfter(newFrob)
            newFrob.setBefore(temp)

def insert_new(atMe, newFrob):
    '''
    1. inserting end
    2. next to atMe
    3. not next to atMe
    '''
    # immediately next to atMe
    if atMe.name[0] <= newFrob.name[0] <= atMe.getAfter().name[0]:
        temp = atMe.getAfter()
        atMe.setAfter(newFrob)
        temp.setBefore(newFrob)

        newFrob.setBefore(atMe)
        newFrob.setAfter(temp)
    # at end
    pointer = atMe
    while pointer.getAfter() != None:
        pointer = pointer.getAfter
    if pointer.name[0] <= newFrob.name[0]:
        pointer.setAfter(newFrob)
        newFrob.setBefore(pointer)

    # TODO not immediately next to atMe
    if atMe.getAfter.name[0] <= newFrob.name[0]:
        pointer = atMe.getAfter()
    if newFrob.name[0] <= atMe.getBefore.name[0]:
        pointer = atMe.getBefore()

def findFront(start):
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())

def walk_through(frob):
    pointer = frob
    chain = []
    while pointer.getBefore() != None:
        pointer = pointer.getBefore()

    while pointer.getAfter() != None:
        chain.append(pointer.name)
        pointer = pointer.getAfter()
    else:
        chain.append(pointer.name)
    return chain
