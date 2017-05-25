import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(n):
    plt.cla()
    r = 0.5
    theta = 2*np.pi/n
    angles = np.arange(1, n+1)*theta
    angles = angles.reshape(-1,1)
    ins_poly = np.hstack((r*np.cos(angles), r*np.sin(angles)))
    ins_poly = np.vstack((ins_poly, ins_poly[0,:]))
    out_poly = np.hstack((r*np.cos(angles)/np.cos(theta/2), r*np.sin(angles)/np.cos(theta/2)))
    for p in out_poly:
        points = np.vstack(([0,0], p))
        plt.plot(points[:,0], points[:,1], '-', color='y')
    out_poly = np.vstack((out_poly, out_poly[0,:]))
    plt.plot(ins_poly[:,0], ins_poly[:,1], '-', color='r', linewidth=2)
    plt.plot(out_poly[:,0], out_poly[:,1], '-', color='b', linewidth=2)
    circle = plt.Circle((0, 0), r, color='k', fill=False, linewidth=2)
    ax = plt.gca()
    ax.add_artist(circle)
    plt.title(r"$%f < \pi < %f \quad n=%d$"%(n*2*r*np.sin(theta/2), n*2*r*np.tan(theta/2),n), fontsize=16)
    plt.axis('equal')
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.tight_layout()

if __name__ == "__main__":
    fig = plt.figure(figsize=(5,5))

    #for i in [6,12,24,48,96]:
    #    animate(i)
    anim = animation.FuncAnimation(fig, animate, frames=np.array([6,12,24,48,96]))
    anim.save('pi.gif', writer='imagemagick', fps=1)
