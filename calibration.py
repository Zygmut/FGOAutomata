from pynput.mouse import Listener, Controller 
from configparser import ConfigParser

def on_click(x, y, button, pressed):
    if not pressed:
        return False
    
def mouse_click_coords():
    with Listener(
        on_click=on_click
    ) as listener:
        mouse = Controller()
        listener.join()

    return mouse.position

''' 
This procedure should get the position all the necessary buttons a basic mission should have and save them in a dictionary type file. Those include, but are not limited to:
 · Servant skills
 · Each attack card and NP
 · Attack button
 · Mystic Code
'''
def calibration():

    print("Calibration procedure")
    print("Click on the leftmost skill of your display")
    
    #First skill 
    f1_click = mouse_click_coords()
    s1_click = mouse_click_coords()
    
    print("First skill is within {0} and {1} on the X axis and {2} and {3} on the y axis".format(
        f1_click[0], s1_click[0], f1_click[1], s1_click[1]
    ))
    
    # Second skill to get overall dimensions and proportions
    f2_click = mouse_click_coords()
    s2_click = mouse_click_coords()
    
    print("Second skill is within {0} and {1} on the X axis and {2} and {3} on the y axis".format(
        f2_click[0], s2_click[0], f2_click[1], s2_click[1]
    ))

    skill_dim = int(s1_click[0] - f1_click[0])
    skill_distance = f2_click[0] - (f1_click[0] + skill_dim)
    inter_servant = int(2.777 * skill_distance)
    print("Skill dimension is about {0}x{0} and skill spacing is {1} and interservant spacing is {2}".format(skill_dim, skill_distance, inter_servant))


    # Once the first area is calibrated, generate all the other coordinates
    config = ConfigParser()
    with open("config.ini", 'r') as configFile:
        config.read(configFile)

    config['Dimensions'] = {}
    config['Dimensions']['skill_dim'] = str(skill_dim)
    config['Dimensions']['skill_dis'] = str(skill_distance)
    config['Dimensions']['servant_dis'] = str(inter_servant)
        
    # One the basic dimensions are done, we'll make the calculation for the first servant
    config["Servant 1"] = {}
    config["Servant 1"]["skill_1"] = ' '.join(str(e) for e in [f1_click[0], f1_click[1], s1_click[0], s1_click[1]])
    config["Servant 1"]["skill_2"] = ' '.join(str(e) for e in [f2_click[0], f2_click[1], s2_click[0], s2_click[1]])
    config["Servant 1"]["skill_3"] = ' '.join(str(e) for e in [f2_click[0] + skill_dim + skill_distance, f2_click[1], s2_click[0] + skill_dim + skill_distance, s2_click[1]])
    


    for i in range(2,4,1): #servant
        config['Servant {0}'.format(i)] = {}
      
    
        config['Servant {0}'.format(i)]["skill_1"] = ' '.join(str(e) for e in [f1_click[0] + (i-1) * ((3*skill_dim) + (2*skill_distance) + inter_servant), f1_click[1], s1_click[0]+ (i-1) * ((3*skill_dim) + (2*skill_distance) + inter_servant), s1_click[1]]) # I hate this
        config['Servant {0}'.format(i)]["skill_2"] = ' '.join(str(e) for e in [f2_click[0] + (i-1) * ((3*skill_dim) + (2*skill_distance) + inter_servant), f2_click[1], s2_click[0]+ (i-1) * ((3*skill_dim) + (2*skill_distance) + inter_servant), s2_click[1]])
        config['Servant {0}'.format(i)]["skill_3"] = ' '.join(str(e) for e in [f2_click[0]+ skill_dim + skill_distance + (i-1) * ((3*skill_dim) + (3*skill_distance) + inter_servant), f2_click[1], s2_click[0]+ skill_dim + skill_distance+ (i-1) * ((3*skill_dim) + (2*skill_distance) + inter_servant), s2_click[1]])
             

    # Convert the String arrayt of numbers of the configfile to int array
    # values2 = [int(num) for num in ' '.join(str(e) for e in values).split()]
    

    # Save file
    with open('config.ini', 'w') as configFile:
        config.write(configFile)

def mouse_coordinate():
    click1 = mouse_click_coords()
    click2 = mouse_click_coords()
    print("x1:{0} y1:{1}\tx2:{2} y2:{3}".format(
        click1[0], click1[1], click2[0], click2[1]
    ))
