from robot_class import robot
from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# --------
# this helper function displays the world that a robot is in
# it assumes the world is a square grid of some given size
# and that landmarks is a list of landmark positions(an optional argument)
def display_world(world_size, position, landmarks=None):
    
    # using seaborn, set background grid to gray
    sns.set_style("dark")

    # Plot grid of values
    world_grid = np.zeros((world_size+1, world_size+1))

    # Set minor axes in between the labels
    ax=plt.gca()
    cols = world_size+1
    rows = world_size+1

    ax.set_xticks([x for x in range(1,cols)],minor=True )
    ax.set_yticks([y for y in range(1,rows)],minor=True)
    
    # Plot grid on minor axes in gray (width = 1)
    plt.grid(which='minor',ls='-',lw=1, color='white')
    
    # Plot grid on major axes in larger width
    plt.grid(which='major',ls='-',lw=2, color='white')
    
    # Create an 'o' character that represents the robot
    # ha = horizontal alignment, va = vertical
    ax.text(position[0], position[1], 'o', ha='center', va='center', color='r', fontsize=30)
    
    # Draw landmarks if they exists
    if(landmarks is not None):
        # loop through all path indices and draw a dot (unless it's at the car's location)
        for pos in landmarks:
            if(pos != position):
                ax.text(pos[0], pos[1], 'x', ha='center', va='center', color='purple', fontsize=20)
    
    # Display final result
    plt.show()


# --------
# This helper function displays the 2D world that a robot is in from its perspective compared to ground truth.
# It assumes the world is a square grid of some given size.
# It expects the world size, initial robot position, the estimated final robot position affected by motion noise, 
# the true noise-free final robot position (ground truth), the list of estimted landmark positions affected by 
# measurement noise (optional argument) and the list of true noise-free landmark positions (ground truth).
def display_world_with_ground_truth(world_size, 
                                    initial_position, 
                                    estimated_position, 
                                    true_position, 
                                    estimated_landmarks=None, 
                                    true_landmarks=None):
    
    # using seaborn, set background grid to gray
    sns.set_style("dark")

    # Plot grid of values
    world_grid = np.zeros((world_size+1, world_size+1))

    # Set minor axes in between the labels
    ax=plt.gca()
    cols = world_size+1
    rows = world_size+1

    ax.set_xticks([x for x in range(1,cols)],minor=True )
    ax.set_yticks([y for y in range(1,rows)],minor=True)
    
    # Plot grid on minor axes in gray (width = 1)
    plt.grid(which='minor',ls='-',lw=1, color='white')
    
    # Plot grid on major axes in larger width
    plt.grid(which='major',ls='-',lw=2, color='white')
    
    # Create an 'o' character that represents the robot
    # ha = horizontal alignment, va = vertical
    #ax.text(initial_position[0], initial_position[1], '*', ha='center', va='center', color='b', fontsize=30)
    #ax.text(estimated_position[0], estimated_position[1], 'o', ha='center', va='center', color='r', fontsize=30)
    #ax.text(true_position[0], true_position[1], 'o', ha='center', va='center', color='g', fontsize=30)
    plt.scatter(initial_position[0], initial_position[1], s=100, c='g', marker='*', label='initial position')
    plt.scatter(estimated_position[0], estimated_position[1], s=100, c='r', marker='o', label='estimated final position')
    plt.scatter(true_position[0], true_position[1], s=100, c='g', marker='o', alpha=0.5, label='true final position')
    
    # Draw estimated landmarks if they exists
    if(estimated_landmarks is not None):
        # loop through all path indices and draw a dot
        X, Y = [], []
        for landmark in estimated_landmarks:
            X.append(landmark[0])
            Y.append(landmark[1])
        plt.scatter(X, Y, s=100, c='purple', marker='X', alpha=0.5, label='estimated landmarks')
        #for landmark in estimated_landmarks:
        #    ax.text(landmark[0], landmark[1], 'x', ha='center', va='center', color='purple', fontsize=20)
    
    # Draw true landmarks if they exists
    if(true_landmarks is not None):
        # loop through all path indices and draw a plus
        X, Y = [], []
        for landmark in true_landmarks:
            X.append(landmark[0])
            Y.append(landmark[1])
        plt.scatter(X, Y, s=100, c='g', marker='x', alpha=0.5, label='true landmarks')
        #for landmark in true_landmarks:
        #    ax.text(landmark[0], landmark[1], 'x', ha='center', va='center', color='k', fontsize=20)
    
    # Add legend
    ax.legend(loc='best')
    
    # Display final result
    plt.show()


# --------
# this routine makes the robot data
# the data is a list of measurements and movements: [measurements, [dx, dy]]
# collected over a specified number of time steps, N
#
def make_data(N, num_landmarks, world_size, measurement_range, motion_noise, 
              measurement_noise, distance):
    # N = number of robot positions resp. motion steps
    # num_landmarks = number of landmarks in the 2D world
    # world_size = size of the squared 2D world
    # measurement_range = maximum measurement / visibility range of the robot to perceive landmarks
    # motion_noise = motion measurement noise bandwidth
    # measurement_noise = landmark measurement noise bandwidth
    # distance = distance travelled per motion step

    # check that data has been made
    try:
        check_for_data(num_landmarks, world_size, measurement_range, motion_noise, measurement_noise)
    except ValueError:
        print('Error: You must implement the sense function in robot_class.py.')
        return []
    
    complete = False
    
    # initialize 2D world with a robot at its center coordinates
    r = robot(world_size, measurement_range, motion_noise, measurement_noise)
    
    # create random landmarks within the 2D world of the robot
    r.make_landmarks(num_landmarks)
    
    # get true landmark positions
    true_landmarks = r.landmarks
    
    while not complete:
        
        data = []
        
        seen = [False for row in range(num_landmarks)]
        
        # guess an initial motion
        orientation = random.random() * 2.0 * pi
        dx = cos(orientation) * distance
        dy = sin(orientation) * distance
        
        for k in range(N-1):
            
            # collect sensor measurements in a list, Z
            Z = r.sense()
            
            # check off all landmarks that were observed 
            for i in range(len(Z)):
                seen[Z[i][0]] = True
            
            # move (returns False when leaving the robot's 2D world)
            while not r.move(dx, dy):
                # if we'd be leaving the robot world, pick instead a new direction
                orientation = random.random() * 2.0 * pi
                dx = cos(orientation) * distance
                dy = sin(orientation) * distance
            
            # collect/memorize all sensor and motion data
            data.append([Z, [dx, dy]])
        
        # we are done when all landmarks were observed; otherwise re-run
        complete = (sum(seen) == num_landmarks)
        
        # get true robot positions (without motion noise) for reference
        true_positions = r.true_positions
        
    print(' ')
    print('Landmarks: ', r.landmarks)
    print(r)
    
    # return noise-affected measurement data containing [estimted_landmarks, estimated_position]
    # for each motion step plus true landmark positions and true robot positions for reference
    return data, true_landmarks, true_positions


def check_for_data(num_landmarks, world_size, measurement_range, motion_noise, measurement_noise):
    # make robot and landmarks
    r = robot(world_size, measurement_range, motion_noise, measurement_noise)
    r.make_landmarks(num_landmarks)
    
    # check that sense has been implemented/data has been made
    test_Z = r.sense()
    if(test_Z is None):
        raise ValueError
