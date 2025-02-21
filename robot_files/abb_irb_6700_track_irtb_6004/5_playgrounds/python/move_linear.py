import compas_rrc as rrc
from compas.geometry import Frame, Point, Vector


if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print text on FlexPenant
    done = abb.send_and_wait(rrc.PrintText('Welcome to COMPAS_RRC'))

    # Set tool
    #abb.send(rrc.SetTool('tool0'))
    abb.send(rrc.SetTool('ibois_gripper_rotation'))

    # Set work object
    abb.send(rrc.SetWorkObject('wobj0'))

    # Get frame and external axes 
    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())


    # Print received values
    print(frame, external_axes)

    # Change the x-value [mm]
    frame_0 = Frame(Point(7000, 1500, 1500), Vector(0, 1, 0), Vector(1, 0,0))
    frame_1 = Frame(Point(7000, 1500, 0), Vector(1,0,0), Vector(0,-1,0))
    frame_2 = Frame(Point(7000, 1500, -640), Vector(1,0,0), Vector(0,-1,0))
    frame_3 = Frame(Point(7000, 1500, 1500), Vector(1,0,0), Vector(0,-1,0))


    print(frame_0)

    # Set speed [mm/s]
    speed = 200

    # Move robot the new pos
    
    abb.send_and_wait(rrc.MoveToFrame(frame_0, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))
    abb.send_and_wait(rrc.MoveToFrame(frame_1, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))
    abb.send_and_wait(rrc.MoveToFrame(frame_2, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))
    abb.send_and_wait(rrc.MoveToFrame(frame_3, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))


    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')
 
    # Close client
    ros.close()
    ros.terminate()
