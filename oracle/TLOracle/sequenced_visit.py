
# MIT License
#
# Copyright (c) [2020] [Angelo Ferrando]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import getpass
current_user = getpass.getuser()
pointlib_path = "/home/{0}/catkin_ws/shared_python".format(current_user)
sys.path.insert(0,pointlib_path)
from Point import CPoint
from Point import LOCATIONS

from LocReached import LocationProps
from LocReached import LocationsReached


import math
import oracle

ERROR_THRESHOLD=0.5
locobjs = LocationsReached(ERROR_THRESHOLD)

l1 = 'pipes'
l2 = 'tank1top'
l3 = 'bigtankfront'


# property to verify
PROPERTY = "(( once ( {{{2}:true}} and ( once ( {{{1}:true}} and (once{{{0}:true}})  )  )  ) ))".format(l1,l2,l3)
#"once{{{0}:true}} and once{{{1}:true}} and once{{{2}:true}}".format(l1,l2,l3)

property_locations=[l1,l2,l3]

# predicates used in the property (initialization for time 0)
predicates = dict(
    time = 0,
    tank1top = False,
    bigtankfront = False,
    pipes = False
)
# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates
def abstract_message(message):
    

    current_point = CPoint(message['x'],message['y'],message['z'])
    
    # for loc in property_locations:
    #     loc_point = LOCATIONS[loc]
    #     dist = loc_point.distance(current_point)
    #     print(dist)
    #     if (dist < ERROR_THRESHOLD):
    #         predicates[loc] = True
    #         print(loc+' found')
    #         print(predicates)
    #     else:
    #         predicates[loc] = False
    t = message['time']

    for loc in property_locations:
        #loc_point = LOCATIONS[loc]
        #dist = loc_point.distance(current_point)
        #print(dist)
        #if (dist < ERROR_THRESHOLD):
        #    predicates[loc] = True
        #    print(loc+' found')
        #    print(predicates)
        #else:
        #    predicates[loc] = False
        loc_point = locobjs.get_loc_object(loc)
        if loc_point.has_reached_location(current_point,t):
            predicates[loc] = True
            print("{0} found".format(loc))
            print(predicates)
        else:
            predicates[loc] = False 

        
    predicates['time'] = message['time']
    

    return predicates
# This function has to be defined by the user depending on the property defined.
# In this case we have just implemented a simple and general function which
# updates the predicates if it finds the topic in the list of predicates.
# Since the property is defined on predicates, we need this function to update the
# predicates each time a message is observed. This abstraction of course is totally
# dependent on the specific application.
