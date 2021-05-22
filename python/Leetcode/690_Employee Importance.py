'''
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.
For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

ex1
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
'''
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution:
    total = 0
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        employees = {e.id: e for e in employees}
        queue = collections.deque([id])
        def dfs(e_id):
            if e_id not in employees:
                return
            self.total += employees[e_id].importance
            for i in employees[e_id].subordinates:
                dfs(i)
            return
        dfs(id)
        return self.total

