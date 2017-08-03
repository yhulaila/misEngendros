KPL/MK

Meta-kernel for the Rosetta dataset release v0.3.0            
==========================================================================

   This meta-kernel lists the Rosetta SPICE kernels providing coverage 
   for the full mision. All of the kernels listed below are stored in 
   the Rosetta SPICE Dataset. This set of files and the order in which 
   they are listed were picked to provide the best available data and 
   the most complete coverage based on the information about the kernels 
   available at the time this meta-kernel was produced.


Usage of the Meta-kernel
-------------------------------------------------------------------------

   This meta-kernel lists the Rosetta SPICE kernels providing coverage
   for the full mission.

      Summary for: ../spk/ORHR___________T19_00122.BSP
       
      Body: ROSETTA ORBITER (-226)
            Start of Interval (ET)              End of Interval (ET)
            -----------------------------       -----------------------------
            2004 MAR 02 09:26:21.583            2014 AUG 04 01:16:37.085
       
       
      Summary for: ../spk/former_versions/RORB_DV_145_01___T19_00216.BSP
       
      Body: ROSETTA ORBITER (-226)
            Start of Interval (ET)              End of Interval (ET)
            -----------------------------       -----------------------------
            2014 JAN 01 00:00:00.000            2015 OCT 31 01:41:08.182
       
       
      Summary for: ../spk/former_versions/RORB_DV_223_01___T19_00302.BSP
       
      Body: ROSETTA ORBITER (-226)
            Start of Interval (ET)              End of Interval (ET)
            -----------------------------       -----------------------------
            2015 MAR 01 00:00:00.000            2016 JUL 17 01:41:08.183
       
       
      Summary for: ../spk/RORB_DV_257_02___T19_00344.BSP
       
      Body: ROSETTA ORBITER (-226)
            Start of Interval (ET)              End of Interval (ET)
            -----------------------------       -----------------------------
            2015 DEC 31 21:58:59.183            2016 OCT 05 00:01:08.182
       
       
      Summary for: ../spk/ROS_ORBITER_EXTENSION_V1.BSP
       
      Body: ROSETTA ORBITER (-226)*
            Start of Interval (ET)              End of Interval (ET)
            -----------------------------       -----------------------------
            2016 OCT 05 00:01:08.181            2017 JAN 01 00:08:51.000
      

   Reading the comments of the binary SPK and C-Kernels is very helpful to
   understand the implemented SC position and orientation. You can use the
   following NAIF command line utility to extract that information from the
   kernels:

      > commnt -r RATT_*.bc

   The kernels listed below can be found at:

      ftp://ssols01.esac.esa.int/pub/data/SPICE/ROSETTA/kernels/

   It is recommended that users make a local copy of this file and
   modify the value of the PATH_VALUES keyword to point to the actual
   location of the Mars Express SPICE ``data'' directory on their
   system. Replacing ``/'' with ``\'' and converting line terminators
   to the format native to the user's system may also be required if
   this meta-kernel is to be used on a non-UNIX workstation.
   

Implementation Notes
-------------------------------------------------------------------------    

   It is recommended that users make a local copy of this file and
   modify the value of the PATH_VALUES keyword to point to the actual
   location of the ROSETTA SPICE data set's ``data'' directory on 
   their system. Replacing ``/'' with ``\'' and converting line 
   terminators to the format native to the user's system may also be 
   required if this meta-kernel is to be used on a non-UNIX workstation.

-------------------   

   This file was created on March 30, 2017 by Marc Costa Sitja ESAC/ESA.


   \begindata

     PATH_VALUES       = ( '/mnt/PhD/spice/kernels'  )

     PATH_SYMBOLS      = ( 'KERNELS' )

     KERNELS_TO_LOAD   = (

                          '$KERNELS/lsk/NAIF0011.TLS'


                          '$KERNELS/sclk/ROS_160929_STEP.TSC'


                          '$KERNELS/pck/PCK00010.TPC'
                          '$KERNELS/pck/DE403_MASSES.TPC'
                          '$KERNELS/pck/former_versions/EARTH_000101_170227_161206.BPC'

                          '$KERNELS/pck/ROS_LUTETIA_RSOC_V03.TPC'
                          '$KERNELS/pck/ROS_STEINS_V05.TPC'
                          '$KERNELS/pck/ROS_STEINS_V05.TPC'
                          '$KERNELS/pck/ROS_CG_RAD_V10.TPC'


                          '$KERNELS/fk/EARTHFIXEDITRF93.TF'
                          '$KERNELS/fk/EARTH_TOPO_050714.TF'
                          '$KERNELS/fk/ESTRACK_V01.TF'
                          '$KERNELS/fk/NEW_NORCIA_TOPO.TF'

                          '$KERNELS/fk/ROS_LUTETIA_RSOC_V03.TF'

                          '$KERNELS/fk/RSSD0002.TF'

                          '$KERNELS/fk/ROS_V27.TF'


                          '$KERNELS/ik/ROS_ALICE_V16.TI'
                          '$KERNELS/ik/ROS_CIVA_V10.TI'
                          '$KERNELS/ik/ROS_CONSERT_V11.TI'
                          '$KERNELS/ik/ROS_COSIMA_V13.TI'
                          '$KERNELS/ik/ROS_DIM_V11.TI'
                          '$KERNELS/ik/ROS_GIADA_V12.TI'
                          '$KERNELS/ik/ROS_MIDAS_V10.TI'
                          '$KERNELS/ik/ROS_MIRO_V10.TI'
                          '$KERNELS/ik/ROS_NAVCAM_V01.TI'
                          '$KERNELS/ik/ROS_OSIRIS_V13.TI'
                          '$KERNELS/ik/ROS_ROLIS_V03.TI'
                          '$KERNELS/ik/ROS_ROSINA_V12.TI'
                          '$KERNELS/ik/ROS_RPC_V18.TI'
                          '$KERNELS/ik/ROS_STR_V11.TI'
                          '$KERNELS/ik/ROS_VIRTIS_V13.TI'


                          '$KERNELS/spk/DE405.BSP'
                          '$KERNELS/spk/OUTERPLANETS_V0002.BSP'

                          '$KERNELS/spk/EARTHSTNS_ITRF93_050714.BSP'
                          '$KERNELS/spk/ESTRACK_V01.BSP'
                          '$KERNELS/spk/NEW_NORCIA.BSP'

                          '$KERNELS/spk/TEMPEL1_9P_DI_P.BSP'

                          '$KERNELS/spk/former_versions/21_LUTETIA_2004_2016.BSP'
                          '$KERNELS/spk/ORHS_______________00109.BSP'

                          '$KERNELS/spk/former_versions/2867_STEINS_2004_2016.BSP'
                          '$KERNELS/spk/ORHO_______________00077.BSP'

                          '$KERNELS/spk/former_versions/ORHW_______________00016.BSP'
                          '$KERNELS/spk/ORHW_______________00122.BSP'
                          '$KERNELS/spk/former_versions/CORB_DV_145_01___T19_00216.BSP'
                          '$KERNELS/spk/former_versions/CORB_DV_223_01___T19_00302.BSP'
                          '$KERNELS/spk/CORB_DV_257_02___T19_00344.BSP' 

                          '$KERNELS/spk/ROS_STRUCT_V5.BSP'

                          '$KERNELS/spk/former_versions/LORB_DV_145_01___T19_00216.BSP'
                          '$KERNELS/spk/former_versions/LORB_DV_223_01___T19_00302.BSP'
                          '$KERNELS/spk/LORB_DV_236_01___T19_00318.BSP'   

                          '$KERNELS/spk/ORHR___________T19_00122.BSP'
                          '$KERNELS/spk/former_versions/RORB_DV_145_01___T19_00216.BSP'
                          '$KERNELS/spk/former_versions/RORB_DV_223_01___T19_00302.BSP'
                          '$KERNELS/spk/RORB_DV_257_02___T19_00344.BSP' 

                          '$KERNELS/spk/ROS_ORBITER_EXTENSION_V1.BSP'


                          '$KERNELS/ck/ROS_LBOOM_V0.BC'

                          '$KERNELS/ck/ROS_HGA_2004_V0001.BC'
                          '$KERNELS/ck/ROS_HGA_2005_V0001.BC'
                          '$KERNELS/ck/ROS_HGA_2006_V0001.BC'
                          '$KERNELS/ck/ROS_HGA_2007_V0001.BC'
                          '$KERNELS/ck/ROS_HGA_2008_V0019.BC'
                          '$KERNELS/ck/ROS_HGA_2009_V0052.BC'
                          '$KERNELS/ck/ROS_HGA_2010_V0046.BC'
                          '$KERNELS/ck/ROS_HGA_2011_V0018.BC'
                          '$KERNELS/ck/ROS_HGA_2014_V0044.BC'
                          '$KERNELS/ck/ROS_HGA_2015_V0053.BC'
                          '$KERNELS/ck/ROS_HGA_2016_V0042.BC'

                          '$KERNELS/ck/ROS_SA_2004_V0001.BC'
                          '$KERNELS/ck/ROS_SA_2005_V0001.BC'
                          '$KERNELS/ck/ROS_SA_2006_V0001.BC'
                          '$KERNELS/ck/ROS_SA_2007_V0001.BC'
                          '$KERNELS/ck/ROS_SA_2008_V0038.BC'
                          '$KERNELS/ck/ROS_SA_2009_V0054.BC'
                          '$KERNELS/ck/ROS_SA_2010_V0052.BC'
                          '$KERNELS/ck/ROS_SA_2011_V0020.BC'
                          '$KERNELS/ck/ROS_SA_2014_V0047.BC'
                          '$KERNELS/ck/ROS_SA_2015_V0042.BC'
                          '$KERNELS/ck/ROS_SA_2016_V0041.BC'

                          '$KERNELS/ck/ROS_VIRTIS_M_0403_1509_V1.BC'
                          '$KERNELS/ck/ROS_VIRTIS_M_1509_1609_V1.BC'

                          '$KERNELS/ck/ATNR_P040302093352_T6_00127.BC'
                          '$KERNELS/ck/former_versions/RATT_DV_145_01_01_T6_00216.BC'
                          '$KERNELS/ck/former_versions/RATT_DV_223_01_01_T6_00302.BC'
                          '$KERNELS/ck/RATT_DV_257_02_01_T6_00344.BC'

                          '$KERNELS/ck/former_versions/CATT_DV_145_01_______00216.BC'
                          '$KERNELS/ck/former_versions/CATT_DV_223_01_______00302.BC'
                          '$KERNELS/ck/CATT_DV_257_02_______00344.BC'

                          '$KERNELS/ck/ROS_ORBITER_EXTENSION_V1.BC'

                         )

   \begintext


End of MK file.