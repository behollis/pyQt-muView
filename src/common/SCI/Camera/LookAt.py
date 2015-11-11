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

        LookAt()
        LookAt(Vex3 eye, center, up)
        LookAt(float eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)

        void Set(Vex3 eye, center, up)
        void Set(float eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)

        void Get(Vex3& eye, center, up)
        void Get(float& eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)

        inline Vex3 Apply(Vex3& p){ return mat * p; }
        inline Vex3 Apply(float x, y, z){ return mat * Vex3(x,y,z); }

        inline Vex3 Unapply(Vex3& p){ return imat * p; }
        inline Vex3 Unapply(float x, y, z){ return imat * Vex3(x,y,z); }

        inline Vex3 GetEye(){ return eye; }
        inline Vex3 GetCenter(){ return center; }
        inline Vex3 GetUp(){ return up; }
        inline Vex3 GetVD(){ return (center-eye).UnitVector(); }
        inline Vex3 GetRight(){ return cross(center-eye,up).UnitVector(); }

        inline Mat4 GetMatrix(){ return mat; }
        inline Mat4 GetInverseMatrix(){ return imat; }

        LookAt& operator=(LookAt& other)

        void MoveForward(float amt)
        void MoveBackward(float amt)
        void MoveLeft(float amt)
        void MoveRight(float amt)
        void MoveUp(float amt)
        void MoveDown(float amt)
        void RotateLeftRight(float amt)
        void RotateUpDown(float amt)

        void Yaw(float amt)
        void Pitch(float amt)
        void Roll(float amt)
    

        def LookAt():
            mat.LoadIdentity()
            imat.LoadIdentity()
            eye.Set(0,0,0)
            center.Set(0,0,-1)
            up.Set(0,1,0)
        
        def LookAt(float eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
            Vex3 _eye(eyeX,eyeY,eyeZ)
            Vex3 _center(centerX,centerY,centerZ)
            Vex3 _up(upX,upY,upZ)
            
            Set(_eye,_center,_up)
        
        def LookAt(Vex3 _eye, _center, _up):
            Set(_eye,_center,_up)
        
        
        def Set(float eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
            Vex3 _eye(eyeX,eyeY,eyeZ)
            Vex3 _center(centerX,centerY,centerZ)
            Vex3 _up(upX,upY,upZ)
        
        def Set(_eye,_center,_up):
            None
        
        def Set(Vex3 _eye, _center, _up):
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
        
        def Get(Vex3& _eye, _center, _up):
            _eye = eye
            _center = center
            _up = up
        
        def Get(float& eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
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
        
        def MoveForward(float amt):
            md = (center - eye).UnitVector() * amt
            Set(eye+md,center+md,up)
        
        def MoveBackward(float amt):
            md = (center - eye).UnitVector() * amt
            Set(eye-md,center-md,up)
        
        def MoveLeft(float amt):
            md = cross(up,(center - eye)).UnitVector() * amt
            Set(eye+md,center+md,up)
        
        void LookAt.MoveRight(float amt){
        md = cross(up,(center - eye)).UnitVector() * amt
        Set(eye-md,center-md,up)
        }
        
        void LookAt.MoveUp(float amt){
        md0 = cross(up,(center - eye)).UnitVector()
        md1 = cross(md0,(center - eye)).UnitVector() * amt
        Set(eye+md1,center+md1,up)
        }
        
        void LookAt.MoveDown(float amt){
        md0 = cross(up,(center - eye)).UnitVector()
        md1 = cross(md0,(center - eye)).UnitVector() * amt
        Set(eye-md1,center-md1,up)
        }
        
        void LookAt.RotateLeftRight(float amt){
        Yaw(amt)
        }
        
        void LookAt.RotateUpDown(float amt){
        Pitch(amt)
        }
        
        void LookAt.Yaw(float amt){
        forward = (center - eye).UnitVector()
        right = cross(forward,up).UnitVector()
            nfrwd = forward * .cosf(DEG2RAD(amt)) + right * .sinf(DEG2RAD(amt))
        Set(eye,eye+nfrwd,up)
        }
        
        void LookAt.Pitch(float amt){
        forward = (center - eye).UnitVector()
        right = cross(forward,up).UnitVector()
            nfrwd = forward * .cosf(DEG2RAD(amt)) + up * .sinf(DEG2RAD(amt))
        nup = cross(right,nfrwd).UnitVector()
        Set(eye,eye+nfrwd,nup)
        }
        
        void LookAt.Roll(float amt){
        forward = (center - eye).UnitVector()
        right = cross(forward,up).UnitVector()
            nup = up * .cosf(DEG2RAD(amt)) + right * .sinf(DEG2RAD(amt))
        Set(eye,center,nup)
        }


