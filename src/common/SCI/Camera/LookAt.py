#include <SCI/Mat4.h>
#include <GL/oglCommon.h>
#include <stdio.h>
#define DEG2RAD(deg) ((deg)/180.0f*3.14159265f)
#define RAD2DEG(rad) ((rad)*180.0f/3.14159265f)

class LookAt():
    def __init__(self):
        self.mat    #Mat4
        self.imat   #Mat4
        self.eye    #Vex3
        self.center #Vex3
        self.up     #Vex3
     
    def init(self):   
        None
    
    def LookAt(self):
        mat.LoadIdentity()
        imat.LoadIdentity()
        eye.Set(0,0,0)
        center.Set(0,0,-1)
        up.Set(0,1,0)
    
    def LookAt(self,eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
        Vex3 _eye(eyeX,eyeY,eyeZ)
        Vex3 _center(centerX,centerY,centerZ)
        Vex3 _up(upX,upY,upZ)
        
        Set(_eye,_center,_up)
    
    def LookAt(self, _eye, _center, _up):
        Set(_eye,_center,_up)
    
    
    def Set(self, eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
        Vex3 _eye(eyeX,eyeY,eyeZ)
        Vex3 _center(centerX,centerY,centerZ)
        Vex3 _up(upX,upY,upZ)
    
    def Set(self, _eye,_center,_up):
        None
    
    def Set(self, _eye, _center, _up):
        eye = _eye
        center = _center
        up = _up
        
        f = (center - eye).UnitVector()
        
        up.Normalize()
        
        s = cross(f, up)
        u = cross(s, f)
        
        Mat4 mtmp
        
        mtmp.Row(0,Vex4( s,0))
        mtmp.Row(1,Vex4( u,0))
        mtmp.Row(2,Vex4(-f,0))
        mtmp.Row(3,Vex4(0,0,0,1))
        
        mat  = mtmp * Mat4(Mat4.MAT4_TRANSLATE,-eye.x,-eye.y,-eye.z)
        imat = mat.Inverse()
    
    def Get(self, _eye, _center, _up):
        _eye = eye
        _center = center
        _up = up
    
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
    def LookAt.operator=(LookAt& other){
    Set(other.GetEye(),other.GetCenter(),other.GetUp())
    return (*self)
    }
    '''
    
    def MoveForward(self, amt):
        md = (center - eye).UnitVector() * amt
        Set(eye+md,center+md,up)
    
    def MoveBackward(self, amt):
        md = (center - eye).UnitVector() * amt
        Set(eye-md,center-md,up)
    
    def MoveLeft(self, amt):
        md = cross(up,(center - eye)).UnitVector() * amt
        Set(eye+md,center+md,up)
    
    def MoveRight(self, amt):
        md = cross(up,(center - eye)).UnitVector() * amt
        Set(eye-md,center-md,up)
        
    def MoveUp(self, amt):
        md0 = cross(up,(center - eye)).UnitVector()
        md1 = cross(md0,(center - eye)).UnitVector() * amt
        Set(eye+md1,center+md1,up)
    
    def MoveDown(self, amt):
        md0 = cross(up,(center - eye)).UnitVector()
        md1 = cross(md0,(center - eye)).UnitVector() * amt
        Set(eye-md1,center-md1,up)
    
    def RotateLeftRight(self, amt):
        Yaw(amt)
    
    def RotateUpDown(self, amt):
        Pitch(amt)
    
    def Yaw(self, amt):
        forward = (center - eye).UnitVector()
        right = cross(forward,up).UnitVector()
            nfrwd = forward * .cosf(DEG2RAD(amt)) + right * .sinf(DEG2RAD(amt))
        Set(eye,eye+nfrwd,up)
    
    def Pitch(self, amt):
        forward = (center - eye).UnitVector()
        right = cross(forward,up).UnitVector()
            nfrwd = forward * .cosf(DEG2RAD(amt)) + up * .sinf(DEG2RAD(amt))
        nup = cross(right,nfrwd).UnitVector()
        Set(eye,eye+nfrwd,nup)
    
    def Roll(self, amt):
        forward = (center - eye).UnitVector()
        right = cross(forward,up).UnitVector()
            nup = up * .cosf(DEG2RAD(amt)) + right * .sinf(DEG2RAD(amt))
        Set(eye,center,nup)
            