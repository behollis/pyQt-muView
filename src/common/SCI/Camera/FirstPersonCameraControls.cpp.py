'''
**  Common Library
**  Copyright (C) 2013  Paul Rosen
**
**  This program is free software: you can redistribute it and/or modify
**  it under the terms of the GNU General Public License as published by
**  the Free Software Foundation, version 3 of the License, or
**  (at your option) any later version.
**
**  This program is distributed in the hope that it will be useful,
**  but WITHOUT ANY WARRANTY; without even the implied warranty of
**  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
**  GNU General Public License for more details.
**
**  You should have received a copy of the GNU General Public License
**  along with self program.  If not, see <http:#www.gnu.org/licenses/>.
'''

#include <SCI/Camera/FirstPersonCameraControls.h>

using namespace SCI

FirstPersonCameraControls.FirstPersonCameraControls(Vex3 startPos){
    angleX = PI
    angleY = 0

    dirZ = .cosf(angleX)
    dirX = .sinf(angleX)

    lat.Set(startPos,startPos+Vex3(dirX,0,dirZ),Vex3(0,1,0))
}

FirstPersonCameraControls.~FirstPersonCameraControls(void){

}

void FirstPersonCameraControls.ResetView(Vex3 startPos){
    angleX = PI
    angleY = 0

    dirZ = .cosf(angleX)
    dirX = .sinf(angleX)

    lat.Set(startPos,startPos+Vex3(dirX,0,dirZ),Vex3(0,1,0))
}


void FirstPersonCameraControls.LookLeft(float amount){
    angleX += amount

    dirX = .sinf(angleX)*.cosf(angleY)
    dirY = .sinf(angleY)
    dirZ = .cosf(angleX)*.cosf(angleY)

    vd = Vex3(dirX,dirY,dirZ).UnitVector()
    tmpX = cross(vd,Vex3(0,1,0)).UnitVector()
    up = cross(tmpX,vd).UnitVector()

    lat.Set(lat.GetEye(),lat.GetEye()+vd,up)
}

void FirstPersonCameraControls.LookRight(float amount){
    angleX -= amount

    dirX = .sinf(angleX)*.cosf(angleY)
    dirY = .sinf(angleY)
    dirZ = .cosf(angleX)*.cosf(angleY)

    vd = Vex3(dirX,dirY,dirZ).UnitVector()
    tmpX = cross(vd,Vex3(0,1,0)).UnitVector()
    up = cross(tmpX,vd).UnitVector()

    lat.Set(lat.GetEye(),lat.GetEye()+vd,up)
}

void FirstPersonCameraControls.LookUp(float amount){ 
    angleY -= amount
    angleY = Clamp(angleY,-1.5f,1.5f)

    dirX = .sinf(angleX)*.cosf(angleY)
    dirY = .sinf(angleY)
    dirZ = .cosf(angleX)*.cosf(angleY)

    vd = Vex3(dirX,dirY,dirZ).UnitVector()
    tmpX = cross(vd,Vex3(0,1,0)).UnitVector()
    up = cross(tmpX,vd).UnitVector()

    lat.Set(lat.GetEye(),lat.GetEye()+vd,up)
}

void FirstPersonCameraControls.LookDown(float amount){ 
    angleY -= amount
    angleY = Clamp(angleY,-1.5f,1.5f)

    dirX = .sinf(angleX)*.cosf(angleY)
    dirY = .sinf(angleY)
    dirZ = .cosf(angleX)*.cosf(angleY)

    vd = Vex3(dirX,dirY,dirZ).UnitVector()
    tmpX = cross(vd,Vex3(0,1,0)).UnitVector()
    up = cross(tmpX,vd).UnitVector()

    lat.Set(lat.GetEye(),lat.GetEye()+vd,up)
}

void FirstPersonCameraControls.MoveForward(float amount){
    vd = lat.GetVD()
    md = Vex3(vd.x,0,vd.z).UnitVector()
    new_eye = lat.GetEye()+md*amount

    lat.Set(new_eye,new_eye+vd,lat.GetUp())
}

void FirstPersonCameraControls.MoveBackward(float amount){
    vd = lat.GetVD()
    md = Vex3(vd.x,0,vd.z).UnitVector()
    new_eye = lat.GetEye()-md*amount

    lat.Set(new_eye,new_eye+vd,lat.GetUp())
}

void FirstPersonCameraControls.MoveLeft(float amount){
    vd = lat.GetVD()
    md = Vex3(vd.x,0,vd.z).UnitVector()
    right = cross(md,Vex3(0,1,0))
    new_eye = lat.GetEye()-right*amount

    lat.Set(new_eye,new_eye+vd,lat.GetUp())
}

void FirstPersonCameraControls.MoveRight(float amount){
    vd = lat.GetVD()
    md = Vex3(vd.x,0,vd.z).UnitVector()
    right = cross(md,Vex3(0,1,0))
    new_eye = lat.GetEye()+right*amount

    lat.Set(new_eye,new_eye+vd,lat.GetUp())
}

void FirstPersonCameraControls.SetEye(Vex3 new_eye){
    lat.Set(new_eye,new_eye+lat.GetVD(),lat.GetUp())
}

void FirstPersonCameraControls.MoveUp(float amount){
    vd = lat.GetVD()
    new_eye = lat.GetEye()+Vex3(0,1,0)*amount
    lat.Set(new_eye,new_eye+vd,lat.GetUp())
}

void FirstPersonCameraControls.MoveDown(float amount){
    vd = lat.GetVD()
    new_eye = lat.GetEye()-Vex3(0,1,0)*amount
    lat.Set(new_eye,new_eye+vd,lat.GetUp())
}

bool FirstPersonCameraControls.Save( char * fname){
    FILE * outfile

    #if(fopen_s(&outfile,fname,"w") == 0){
    if( (outfile=fopen(fname,"w")) != 0){
        fprintf(outfile,"%f %f\n",angleX,angleY)
        fprintf(outfile,"%f %f %f\n",lat.GetEye().x,lat.GetEye().y,lat.GetEye().z)
        fprintf(outfile,"%f %f %f\n",lat.GetCenter().x,lat.GetCenter().y,lat.GetCenter().z)
        fprintf(outfile,"%f %f %f\n",lat.GetUp().x,lat.GetUp().y,lat.GetUp().z)
        fclose(outfile)
        return True
    }
    return False
}

bool FirstPersonCameraControls.Load( char * fname){
    FILE * infile

    #if(fopen_s(&infile,fname,"r") == 0){
    if( (infile=fopen(fname,"r")) != 0){
        Vex3 eye,cen,up
        if( fscanf(infile," %f %f ",   &angleX, &angleY )        != 2 ) printf("WARNING: FirstPersonCameraControls.Load Error\n")
        if( fscanf(infile," %f %f %f ",&eye.x,  &eye.y, &eye.z ) != 3 ) printf("WARNING: FirstPersonCameraControls.Load Error\n")
        if( fscanf(infile," %f %f %f ",&cen.x,  &cen.y, &cen.z ) != 3 ) printf("WARNING: FirstPersonCameraControls.Load Error\n")
        if( fscanf(infile," %f %f %f ",&up.x,   &up.y,  &up.z  ) != 3 ) printf("WARNING: FirstPersonCameraControls.Load Error\n")
        fclose(infile)
        lat.Set(eye,cen,up)
        return True
    }
    return False
}

