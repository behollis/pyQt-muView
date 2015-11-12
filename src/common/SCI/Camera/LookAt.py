#include <SCI/Mat4.h>
#include <GL/oglCommon.h>
#include <stdio.h>
#define DEG2RAD(deg) ((deg)/180.0f*3.14159265f)
#define RAD2DEG(rad) ((rad)*180.0f/3.14159265f)

import numpy as np

class LookAt():
    def __init__(self):
        self.mat = None   #Mat4
        self.imat = None  #Mat4
        self.eye = None   #Vex3
        self.center = None #Vex3
        self.up = None    #Vex3
     
    def init(self):   
        None
    
    def LookAt(self,eyeX=None, eyeY=None, eyeZ=None, centerX=None, \
               centerY=None, centerZ=None, upX=None, upY=None, upZ=None):
        
        if eyeX == None and centerX == None and upX == None :
            self.mat.LoadIdentity()
            self.imat.LoadIdentity()
            self.eye = np.ndarray[(0,0,0)]
            self.center = np.ndarray[(0,0,-1)]
            self.up = np.ndarray[(0,1,0)]
        else:
            self._eye = np.array([eyeX,eyeY,eyeZ])
            self._center = np.array([centerX,centerY,centerZ])
            self._up = np.array([upX,upY,upZ])
        
        self.Set(self._eye,self._center,self._up)
   
    '''
    def Set(self, eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
        eye(eyeX,eyeY,eyeZ)
        Vex3 _center(centerX,centerY,centerZ)
        Vex3 _up(upX,upY,upZ)
    '''
    
    '''
    def Set(self, _eye,_center,_up):
        self.eye = _eye
        self.center = _center
        self.up = _up
    '''
    
    def Set(self, _eye, _center, _up):
        eye = _eye
        center = _center
        up = _up
        
        # find unit vector 
        f = np.linalg.norm( self.center - self.eye ) 
        
        # normalize
        up = np.linalg.norm( up )
        
        s = np.cross(f, up)
        u = np.cross(s, f)
        
        mtmp = np.ndarray([0.,0.,0.,0.], \
                          [0.,0.,0.,0.], \
                          [0.,0.,0.,0.], \
                          [0.,0.,0.,0.] )
        
        mtmp[0:] = np.concatenate(s, 0)  #mtmp.Row(0,Vex4( s,0)) 
        mtmp[1:] = np.concatenate(u, 0)  #mtmp.Row(1,Vex4( u,0))
        mtmp[2:] = np.concatenate(-f, 0) #mtmp.Row(2,Vex4(-f,0))
        mtmp[3:] = np.concatenate([0,0,0], 0)   #mtmp.Row(3,Vex4(0,0,0,1))
        
        #mat  = mtmp * np.ndarray Mat4(Mat4.MAT4_TRANSLATE,-eye.x,-eye.y,-eye.z)
        mat = np.ndarray([0.,0.,0.,0.], \
                          [0.,0.,0.,0.], \
                          [0.,0.,0.,0.], \
                          [0.,0.,0.,0.] )
        self.imat = np.linalg.inv(mat)
    
    def Get(self, _eye, _center, _up):
        
        '''
        _eye = eye
        _center = center
        _up = up
        '''
        
        return self.eye, self.center, self.up
    
    '''
    def Get(self, eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
        eyeX = eye.x
        eyeY = eye.y
        eyeZ = eye.z
        
        centerX = center.x
        centerY = center.y
        centerZ = center.z
        
        upX = up.x
        upY = up.y
        upZ = up.z
    '''
    
    '''
    def LookAt.operator=(LookAt& other){
    Set(other.GetEye(),other.GetCenter(),other.GetUp())
    return (*self)
    }
    '''

    def MoveForward(self, amt):
        md = np.linalg.norm(self.center - self.eye) * amt
        self.Set(self.eye+md,self.center+md,self.up)
    
    def MoveBackward(self, amt):
        md = np.linalg.norm(self.center - self.eye) * amt
        self.Set(self.eye-md,self.center-md,self.up)
    
    def MoveLeft(self, amt):
        md = np.linalg.norm( np.cross(self.up,(self.center - self.eye)) ) * amt
        self.Set(self.eye+md,self.center+md,self.up)
    
    def MoveRight(self, amt):
        md = np.cross( self.up, (self.center - self.eye) ) * amt
        self.Set(self.eye-md,self.center-md,self.up)
        
    def MoveUp(self, amt):
        md0 = np.linalg.norm( np.cross(self.up,(self.center - self.eye)) )
        md1 = np.linalg.norm( np.cross(md0,(self.center - self.eye)) ) * amt
        self.Set(self.eye+md1,self.center+md1,self.up)
    
    def MoveDown(self, amt):
        md0 = np.linalg.norm( np.cross(self.up,(self.center - self.eye)) )
        md1 = np.linalg.norm( np.cross(md0,(self.center - self.eye)) ) * amt
        self.Set(self.eye-md1,self.center-md1,self.up)
    
    def RotateLeftRight(self, amt):
        self.Yaw(amt)
    
    def RotateUpDown(self, amt):
        self.Pitch(amt)
    
    def Yaw(self, amt):
        forward = np.linalg.norm( (self.center - self.eye) ) #UnitVector()
        right = np.linalg.norm( np.cross(forward, self.up) ) #UnitVector()
        nfrwd = forward * np.cos(np.radians(amt)) + right * np.sin(np.radians(amt))
        self.Set(self.eye,self.eye+nfrwd,self.up)
    
    def Pitch(self, amt):
        forward = np.linalg.norm(self.center - self.eye) #UnitVector()
        right = np.cross(forward, self.up) #UnitVector()
        nfrwd = forward * np.cos(np.radians(amt)) + self.up * np.sin(np.radians(amt))
        nup = np.linalg.norm( np.cross(right,nfrwd) ) #UnitVector()
        self.Set(self.eye,self.eye+nfrwd,nup)
    
    def Roll(self, amt):
        forward = np.linalg.norm( self.center - self.eye ) #UnitVector()
        right = np.cross(forward, self.up) #UnitVector()
        nup = self.up * np.cos(np.radians(amt)) + right * np.sin(np.radians(amt))
        self.Set(self.eye,self.center,nup)
            