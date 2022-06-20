class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # similar to course schedule with slight modifications
        
        """
        numCourses = 4
        prerequisites: [[1,0],[2,0],[3,1],[3,2]]
        
               -> 1--> 0<-
               |          |
               |          |
               3- - ----->2
        
        temp_dict = {0:[],1:[0],2:[0].3:[1,2]}
        return_list = []
        checked_set = set()
        
        dfs(0):
            temp_dict[0]==[]: 
                return_list = [0]
                checked_set = (0)
                True
                
        dfs(1):
            prereq: 0
            dfs(0):returns True
                0 is already in checked_set
            add 1 to checked_set and return_list
            checked_set = (0,1)
            return_list = [0,1]
            temp_dict[2] = []
            returns True

        dfs(2):
            prereq= 0
            dfs(0)- returns True
            add 2 to checked_set and return_list
            checked_set = (0,1,2)
            return_list = [0,1,2]
            temp_dict[1] = []
            returns True
            
        dfs(3):
            prereq = 1,2
            dfs(1)--returns True
            dfs(2)--returns True
            add 3 to checked_set and return_list
            checked_set = (0,1,2,3)
            return_list = [0,1,2,3]
            temp_dict[3] = []
            returns True
            
            
        Note: temp_set checks if there i cycle in our prerequistes which in case False is returned
            
            
        
        
        
        """
        temp_dict = {course:[] for course in range(numCourses)}
        
        return_list = []
        
        for course, req in prerequisites:
            temp_dict[course].append(req)
            
        temp_set = set()  # to check cycle
        
        checked_ = set()  # to verify if the element has already been visited
  
        
        def dfs(course):
            
            #if the course doesnot have any prerequisit:
            if course in temp_set:
                return False
            if temp_dict[course]==[]:
                if course not in checked_:
                    checked_.add(course)
                    return_list.append(course)
                    
                return True
                
            temp_set.add(course)
            
            for req in temp_dict[course]:
                if not dfs(req): return False
                
            temp_set.remove(course)
            temp_dict[course] = []
            checked_.add(course)
            return_list.append(course)
            
            
            return True
            
        
        for course in range(numCourses):
            if not dfs(course): return []
            
        return return_list