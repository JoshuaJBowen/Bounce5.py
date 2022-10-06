#Bounce5 (Cleaning code, adding a Surface object for clarity, paradigm shift: Ball and Surface interact within main function, not withint the ball)
#Josh Bowen
#5/3/2022

import turtle
import random
import math

#---------------------
# This is a simulation of a ball
# bouncing inside any shape.
#---------------------

class Surface():
    """ One of the two main objects needed for a ball bouncing in a random shape simulation.
        This object will represent the sides of the random shape.
    """
    def __init__(self, identification, first_x, first_y, last_x, last_y):
        """ Constructor method for the Surface class

                indentification can be any value that can be used to indentify one surface from another
                first_x, first_y, last_x, last_y are all integers representing the
                beginning and end of the surface

                for now a valid surface is defined where x_first != x_last or y_first != y_last
        """
        self.id = identification
        
        #coordinates of the start and finish of the surface for quick reference
        self.starting_point = [first_x, first_y]
        self.ending_point = [last_x, last_y]
        
        #represent the linear surface with vector parameterization for consistency
        self.op = [first_x, first_y]
        self.v = [last_x - first_x, last_y - first_y]
        self.range_of_t = [0, 1]


    def __str__(self):
        send_string = "Surface called: " + str(self.id)
        return send_string
    

    def get_id(self):
        """ A fruitful method that returns the surface's
            identification.
        """
        return self.id


    def get_first(self):
        """ A fruitful method that returns the surface's
            starting point.
        """
        return self.starting_point


    def get_last(self):
        """ A fruitful method that returns the surface's
            ending point.
        """
        return self.ending_point
        
    
    def get_op(self):
        """ A fruitful method that returns the surface's
            position vector.
        """
        return self.op


    def get_v(self):
        """ A fruitful method that returns the surface's
            direction vector.
        """
        return self.v

    
    def get_normal(self, point):
        """ A reader method that returns a unit-length normal vector at any given point

                point is a list of two integers representing an x-y point
        """
        normal = [0,0]
        #for a simple line segment the normal is constant regardless of location, unless its on the end point
        #the only tricky part is doing the corners
        
        if point[0] == self.starting_point[0] and point[1] == self.starting_point[1]:##########################################################################
            #find out if this is an inside corner or outside corner or a flat intercept
            #then calculate the corect normal
            print("Still havent done this yet")
            normal = [0,0]
        elif point[0] == self.ending_point[0] and point[1] == self.ending_point[1]:
            #find out if this is an inside corner or outside corner or a flat intercept
            #then calculate the corect normal
            print("Still havent done this yet")
            normal = [0,0]
        else:
            normal =  [-1*self.v[1], self.v[0]]
        
        return [normal[0]/math.sqrt(normal[0]**2 + normal[1]**2), (normal[1])/math.sqrt(normal[0]**2 + normal[1]**2)]       
        

    def intercept_in_bounds(self, intercept):
        """ A writer method that returns boolean values based on if a
            calcualted ball intercept is within the bounds of the surface

                intercept is a list of two integers representing an x-y point
        """
        in_bounds = False
        
        if self.v[0] == 0: #its a vertical surface
            if (intercept[1] - self.op[1])/(self.v[1]) <= self.range_of_t[1] and (intercept[1] - self.op[1])/(self.v[1]) >= self.range_of_t[0]:
                in_bounds = True
        elif self.v[1] == 0: #its a horizontal surface
            if (intercept[0] - self.op[0])/(self.v[0]) <= self.range_of_t[1] and (intercept[0] - self.op[0])/(self.v[0]) >= self.range_of_t[0]:
                in_bounds = True
        else: #check both equations
            print("Calc t value 1:", (intercept[0] - self.op[0])/(self.v[0]), "Calc t value 2:", (intercept[1] - self.op[1])/(self.v[1]))
            if (intercept[1] - self.op[1])/(self.v[1]) <= self.range_of_t[1] and (intercept[1] - self.op[1])/(self.v[1]) >= self.range_of_t[0] and (intercept[0] - self.op[0])/(self.v[0]) == (intercept[1] - self.op[1])/(self.v[1]):
                in_bounds = True

        return in_bounds
                

class Ball():
    """ One of the two main objects needed for a ball bouncing in a random shape simulation.
        This object will represent the ball in the simulation
    """
    def __init__(self, color, speed):
        """ Constructor method for the Ball class

                color is a string of the available Turtle object colors
                surfaces is a list of touples of surfacs of the form (first_x, first_y, last_x, last_y)
                where x_first != x_last or y_first != y_last
        """
        #create a turtle object that is referenceable inside the Ball obejct for graphical representation
        self.turt = turtle.Turtle()
        #self.turt.up()
        self.turt.color(color)
        self.turt.speed(speed)
        self.turt.shape("circle")

        #choose a random angle to orient the Ball to start its bouncing
        theta = random.randrange(0,360)*math.pi/100
        self.op = [0,0]
        
        #V is a direction vector for the ball - named from vector parametrization of lines
        self.v = [math.cos(theta), math.sin(theta)]
        self.t = 0
        self.intercept = [0,0]


    def set_v(self, v):
        """ Writer method that allows the Ball's direction vector
            to be set to a new value.

                v is a list of length two representing a vector
        """
        self.v = v
        print("New direction vector:", self.v)


    def set_op(self, op):
        """ Writer method that allows the Ball's position vector
            to be set to a new value.

                op is a list of length two representing a vector
        """
        self.op = op
        
        
    def set_t(self, t_value):
        """ Writer method that allows the Ball's distance parameterization
            value to be set to a new value.

                t_value is a float
        """
        self.t = t_value


    def set_intercept(self, intercept):
        """ Writer method that allows the Ball's next interception
            point with a surface to be set to a new value.

                intercept is a list of length two representing an x-y point
        """
        self.intercept = intercept


    def move_turt(self):
        """ Graphics method that moves a turtle object to the Ball's
            last position for visualization.
        """
        self.turt.goto(self.intercept)

        
    def get_v(self):
        """ Reader method that returns the Ball's direction vector
        """
        return self.v


    def get_op(self):
        """ Reader method that returns the Ball's position vector
        """
        return self.op
        
    def get_intercept(self):
        """ Reader method that returns the Ball's next calculated intercept
        """
        return self.intercept


    def calculate_t_value(self, surface_list):
        """ Fruitful method for the Ball class. Its purpose is calculating the distance
            the ball must travel before boucning off another surface.

                surface_list is a list of all surface objects
        """
        possible_t_values = {}
        min_t = 0.0

        #find which surfaces the ball is headed towards
        for surface_object in surface_list:
            op_other = surface_object.get_op()
            v_other = surface_object.get_v()
            identification = surface_object.get_id()

            if v_other[1] == 0: #its a horizontal surface
                if (op_other[1] - self.op[1])/(self.v[1]) > 0:
                    self.t = (op_other[1] - self.op[1])/(self.v[1])
                    if surface_object.intercept_in_bounds(self.calculate_intercept()):
                        possible_t_values[identification] = ((op_other[1] - self.op[1])/(self.v[1]))
            elif v_other[0] == 0: #its a vertical surface
                if (op_other[0] - self.op[0])/(self.v[0]) > 0:
                    self.t = (op_other[0] - self.op[0])/(self.v[0])
                    if surface_object.intercept_in_bounds(self.calculate_intercept()):
                        possible_t_values[identification] = ((op_other[0] - self.op[0])/(self.v[0]))
            else: #solved system of 2 equations with s and t for vector parameterizations
                if ((op_other[0] - self.op[0] + (self.op[1]*v_other[0]/v_other[1]) - (op_other[1]*v_other[0]/v_other[1])) / (self.v[0] - (v_other[0]*self.v[1]/v_other[1]))) > 0:
                    self.t = ((op_other[0] - self.op[0] + (self.op[1]*v_other[0]/v_other[1]) - (op_other[1]*v_other[0]/v_other[1])) / (self.v[0] - (v_other[0]*self.v[1]/v_other[1])))
                    if surface_object.intercept_in_bounds(self.calculate_intercept()):
                        possible_t_values[identification] = (((op_other[0] - self.op[0] + (self.op[1]*v_other[0]/v_other[1]) - (op_other[1]*v_other[0]/v_other[1])) / (self.v[0] - (v_other[0]*self.v[1]/v_other[1]))))

        if len(possible_t_values) > 0:
            return min(list(possible_t_values.values()))
        else: #if there are no surfaces the ball will intersect with, return an identifier
            return -1


    def calculate_intercept(self):
        """ Fruitful method for the Ball class. Its purpose is calculating the
            of the ball and the surface it will collide with next.
        """
        return [int(round(self.op[0] + self.v[0]*self.t,0)), int(round(self.op[1] + self.v[1]*self.t,0))]


    def calculate_reflection_vector(self, surface_list):
        """ Fruitful method for the Ball class. Its purpose is calculating the new
            direction vector of the ball after it bounces off a surface.
        """
        surfaces = []
        unit_normal = []
        x = 0
        y = 0

        for surface_object in surface_list:
            if surface_object.intercept_in_bounds(self.op):
                surfaces.append(surface_object)
                print("added an object")

        print(surfaces[0])

        if len(surfaces) > 1:#may be obsolete
            #we are hitting two or more surfaces!!!!!!!!!!!!!!!!!
            print("Still havent done this yet") #################this could be done in the surfaces normal method or here######################################################
            x = -1*self.v[0]
            y = -1*self.v[1]

        else:
            unit_normal = surfaces[0].get_normal(self.op)       
            #Concept from stackoverflow.com
            x = self.v[0] - 2*(self.v[0]*unit_normal[0] + self.v[1]*unit_normal[1])*unit_normal[0]
            y = self.v[1] - 2*(self.v[1]*unit_normal[1] + self.v[0]*unit_normal[0])*unit_normal[1]

        return [x,y]


    def headed_toward_surface(self, t_value):
        """ Fruitful method for the Ball class. Its purpose is indicate if the
            ball is headed to a surface, or if it will continue moving in a
            straight path foreverthe based off of a t_value.
        """
        if t_value > 0:
            return True
        else:
            return False


def main():
    bottom = Surface("bottom-outside", -200, -200, 200, -200)
    right = Surface("right-outside", 200, -200, 200, 200)
    top = Surface("top-outside", 200, 200, -200, 200)
    left = Surface("left-outside", -200, 200, -200, -200)
    
    surfaces = [bottom, right, top, left]
    
    wn = turtle.Screen()
    wn.bgcolor("Black")

    bound = turtle.Turtle()
    bound.color("White")
    bound.speed(0)
    bound.width(5)
    bound.ht()
        
    for surface in surfaces:
        bound.up()
        bound.goto(surface.get_first())
        bound.down()
        bound.goto(surface.get_last())

    speed = 1
    my_ball = Ball("lightblue", speed)
    
    t_value = my_ball.calculate_t_value(surfaces)
    my_ball.set_t(t_value)
    intercept = [0,0]
    op = [0,0]
    v = [0,0]
    
    #while my_ball.headed_toward_surface(t_value):
    for i in range(2):
        intercept = my_ball.calculate_intercept()
        my_ball.set_intercept(intercept)
        my_ball.move_turt()
        my_ball.set_op(intercept)
        my_ball.set_v(my_ball.calculate_reflection_vector(surfaces))
        t_value = my_ball.calculate_t_value(surfaces)
        my_ball.set_t(t_value) 
        
    t_value = 999999
    my_ball.set_t(t_value)
    intercept = my_ball.calculate_intercept()
    my_ball.set_intercept(intercept)
    my_ball.move_turt()
    my_ball.set_op(intercept)
    my_ball.set_v([0,0])
    print("The ball bounced out!")

main()


#---------------------
# TODO for this version:
# Fix the reflection vector/normal vector call
# Allow for ball bouncing off outside corners
# Allow for shapes inside other shapes -- like mini golf on phone
#---------------------

#---------------------
#Goals for future versions:
#user interface - easily define surfaces, maybe input name for ball, its speed, and initial locations and heading
#allow for surfaces to be circles and curves -- mayber intercept should not be a int value?
#make a surface that is associated with the balls so they can bouce off each other -- trick: they just swap direction vectors
#Change the speed of the ball as it moves
#---------------------
