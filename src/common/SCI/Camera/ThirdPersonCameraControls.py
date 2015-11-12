#ifndef SCI_CAMERA_THIRDPERSONCAMERACONTROLS_H
#define SCI_CAMERA_THIRDPERSONCAMERACONTROLS_H

#include <SCI/Camera/CameraControls.h>
#include <SCI/Camera/LookAt.h>
#include <SCI/Camera/ThirdPersonCameraControls.h>

from common.SCI.Camera.CameraControls import CameraControls
from common.SCI.Camera.LookAt import LookAt
from common.SCI.Mat4 import Mat4

import numpy as np

'''   
ThirdPersonCameraControls(startAngleX = 0.0f, startAngleY = 45.0f, startDistance = 40.0f, startCenter = Vex3(0,0,0), up = Vex3(0,1,0))
 ~ThirdPersonCameraControls(void)
 void Set(startAngleX = 0.0f, startAngleY = 45.0f, startDistance = 40.0f, startCenter = Vex3(0,0,0), up = Vex3(0,1,0))
 Mat4 GetView()
 void Rotate(float amtX, amtY)
 void Translate(float amtX, amtY)
 void Zoom(float amt)
 bool Save( char* fname)
 bool Load( char* fname)
 float GetAngleX(){ return AngleX; }
 float GetAngleY(){ return AngleY; }
 Vex3 GetEye()
 Vex3 GetVD()
 Vex3 GetRight()
 Vex3 GetUp()
 Vex3 GetCenter()
 void InterpolateView(ThirdPersonCameraControls & v0, & v1, t)
 void SetCenter(Vex3 cen){ Center = cen; _RecalcView(); }
 '''  

class ThirdPersonCameraControls(CameraControls):
    
    def __init__( self, startAngleX = 0.0, startAngleY = 45.0, \
                 startDistance = 40.0, startCenter = np.ndarray([0,0,0]), \
                 up = np.ndarray([0,1,0]) ):
        super(ThirdPersonCameraControls, self).__init__()

        self.DistanceToCenter = 0.
        self.AngleX = 0.
        self.AngleY = 0.

        self.up = np.ndarray([0.,0.,0.])
        self.DirectionToEye = np.ndarray([0.,0.,0.])
        self.Center = np.ndarray([0.,0.,0.])

        self.cs_x  = np.ndarray([0.,0.,0.])
        self.cs_y  = np.ndarray([0.,0.,0.])
        self.cs_z  = np.ndarray([0.,0.,0.])

        lat = LookAt() #LookAt

        self.ThirdPersonCameraControls(startAngleX, startAngleY, startDistance, startCenter, up)

    def SetCenter(self, cen): 
        self.Center = cen 
        self._RecalcView() 
        
    def ThirdPersonCameraControls(self, startAngleX, startAngleY, startDistance, startCenter, _up):
        self.up = _up
    
        self.DistanceToCenter = startDistance
    
        self.AngleX = startAngleX
        self.AngleY = startAngleY
    
        self.DirectionToEye = Mat4(Mat4.MAT4_ROTATION,AngleX,0,1,0) * Mat4(Mat4.MAT4_ROTATION,180.0f-AngleY,1,0,0) * (-up)
    
        self.Center = startCenter
    
        self._RecalcView()

    def Set(self, startAngleX, startAngleY, startDistance, startCenter, _up):

        up = _up
    
        DistanceToCenter = startDistance
    
        AngleX = startAngleX
        AngleY = startAngleY
    
        Center = startCenter
    
        self._RecalcView()

    def _RecalcView(self):
        #DirectionToEye = Mat4(Mat4.MAT4_ROTATION,AngleX,0,1,0) * Mat4(Mat4.MAT4_ROTATION,180.0f-AngleY,1,0,0) * (-up)
    
        cs_z = np.ndarray([0,0,0]) - self.DirectionToEye / np.linalg.norm( self.DirectionToEye ) \
            *  ( self.DirectionToEye / np.linalg.norm( self.DistanceToCenter ) )
        cs_x = np.cross( cs_z, np.ndarray([0,1,0]) )
        cs_y = np.cross( cs_x, cs_z ) / np.linalg.norm( np.cross( cs_x, cs_z ) )
    
        self.lat.Set(np.linalg.norm(self.DirectionToEye) * \
                     self.DistanceToCenter + self.Center, self. Center, cs_y )
    
    def GetView(self):
        return self.lat.GetMatrix()
    
    def GetEye(self):
        return self.DirectionToEye * self.DistanceToCenter + self.Center
    
    def GetVD(self):
        return np.ndarray[ (0,0,0) ] - \
                np.linalg.norm( self.DirectionToEye ) * \
                np.linalg.norm( self.DistanceToCenter)
                
    def GetCenter(self):
        return self.Center
    
    def GetRight( self ):
        return np.cross( self.GetVD(), \
                         np.linalg.norm( np.ndarray( [0, 1, 0] ) ) ) #.UnitVector()
    
    
    def GetUp(self):
        self.cs_x = np.linalg.norm( np.cross( self.cs_z, np.ndarray( [0,1,0] ) ) ) #.UnitVector()
        return np.linalg.norm( np.cross( self.cs_x, self.GetVD() ) ) #.UnitVector()
    
    def Rotate(self, amtX, amtY):
        self.AngleX += amtX / 4.0
        self.AngleY += amtY / 4.0
        
        #self.AngleY = Clamp(AngleY,1.0f,179.0f)
    
        self._RecalcView()
    
    def Translate(self, amtX, amtY):
        self.Center -= self.cs_x * self.amtX * self.DistanceToCenter / 700.0
        self.Center -= self.cs_y * amtY * self.DistanceToCenter / 700.0
        self._RecalcView( self )
    
    def Zoom(self, amt):
        self.DistanceToCenter *= np.power(1.01,amt)
        if(self.DistanceToCenter < 0.1):
            self.Center -= self.cs_z * amt / 20.0
            self.DistanceToCenter = 0.1
        
        self._RecalcView()
      
    '''  
    def Load( char* fname){
        FILE* infile
        #if(fopen_s(&infile,fname,"r") != 0){ return False; }
        if( (infile=fopen(fname,"r")) == 0){ return False; }
        if( fscanf(infile," %*s %f ",      &DistanceToCenter)             != 1 ) printf("WARNING: ThirdPersonCameraControls.Load Error\n")
        if( fscanf(infile," %*s %f ",      &AngleX)                       != 1 ) printf("WARNING: ThirdPersonCameraControls.Load Error\n")
        if( fscanf(infile," %*s %f ",      &AngleY)                       != 1 ) printf("WARNING: ThirdPersonCameraControls.Load Error\n")
        if( fscanf(infile," %*s %f %f %f ",&Center.x,&Center.y,&Center.z) != 3 ) printf("WARNING: ThirdPersonCameraControls.Load Error\n")
        fclose(infile)
        _RecalcView()
        return True
    '''

    '''
    def Save( char* fname){
        FILE* outfile
        #if(fopen_s(&outfile,fname,"w") != 0){ return False; }
        if( (outfile=fopen(fname,"w")) == 0){ return False; }
        fprintf(outfile,"DistanceToCenter %f\n",DistanceToCenter)
        fprintf(outfile,"AngleX %f\n",AngleX)
        fprintf(outfile,"AngleY %f\n",AngleY)
        fprintf(outfile,"Center %f %f %f\n",Center.x,Center.y,Center.z)
        fclose(outfile)
        return True
    
    
    '''
    
    '''
    def InterpolateView(ThirdPersonCameraControls & v0, & v1, t){
        cen = lerp(v0.Center, v1.Center, t)
        angX = lerp(v0.AngleX, v1.AngleX, t)
        angY = lerp(v0.AngleY, v1.AngleY, t)
        dist = lerp(v0.DistanceToCenter, v1.DistanceToCenter, t)
    
        Set( angX, angY, dist, cen, Vex3(0,1,0) )
    
        v0.Save("tmp0.txt")
        v1.Save("tmp1.txt")
        Save("tmp2.txt")
    '''
