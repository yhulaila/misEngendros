import spiops
import spiceypy as cspice

result = spiops.cov_spk_ker('RORB_DV_257_02___T19_00344.BSP',['NAIF0011.TLS',"ROS_V27.TF"],object='ROS', time_format='UTC',report=True)
