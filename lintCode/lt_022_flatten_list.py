class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        flattenedList = []
        return self.__flatten(nestedList, flattenedList)

    def __flatten(self, nestedList, flattenedList):
        if isinstance(nestedList, list):
            for nestedItem in nestedList:
                self.__flatten(nestedItem, flattenedList)
        else:
            flattenedList.append(nestedList)
        return flattenedList
