# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        # https://www.youtube.com/watch?v=-1P3VP7LH0I
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
        
        visited = set()
        
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def backTrack(x,y,direction):
            visited.add((x,y))
            robot.clean()
            
            # go in all four directtions
            for i in range(4):
                new_direction = (direction+i) % 4
                
                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1]
                
                if (new_x,new_y) not in visited and robot.move():
                    backTrack(new_x,new_y, new_direction)
                    goBack()
                    
                robot.turnRight()
                
        backTrack(0,0,0)
                
                
        
        
        """
        0 => going up
        1 => going right
        2 => going down
        3 => going left
        
        lets say our current_direction is going up
        from there we can go up,right , down or left
        eg: if we are at 3 going left, we want to go further left,
        
        
        N = number of tiles in room
        M = number of obstacles
        Time complexity: 0(N-M)
        Space complexity: 0(N-M)
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        