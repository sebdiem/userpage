# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Display matplotlib animations as HTML5 video
# 
# Based on [this notebook](http://nbviewer.ipython.org/url/jakevdp.github.io/downloads/notebooks/AnimationEmbedding.ipynb) by jakevdp. Updated with:
# 
#  - output video that works with chrome (pix_fmt below)
#  - add plt.close() to avoid showing PNG below the animation
#  - autoplay (customize the VIDEO_TAG below to change behavior, for example add loop attribute)

# <codecell>

from matplotlib import animation, pyplot as plt
from tempfile import NamedTemporaryFile

VIDEO_TAG = """<video controls autoplay>
 <source src="data:{0}">
 Your browser does not support the video tag.
</video>"""

def anim_to_html(anim):
    if not hasattr(anim, '_encoded_video'):
        with NamedTemporaryFile(suffix='.m4v') as f:
            anim.save(f.name, fps=20, extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
            video = open(f.name, "rb").read()
        anim._encoded_video = 'video/mp4;base64,' + video.encode("base64")
    # prevent figure displayed as a PNG below the animation
    plt.close()
    
    return VIDEO_TAG.format(anim._encoded_video)

from IPython.display import HTML

def display_animation(anim):
    plt.close(anim._fig)
    return HTML(anim_to_html(anim))
