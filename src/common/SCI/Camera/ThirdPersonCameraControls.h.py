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

#ifndef SCI_CAMERA_THIRDPERSONCAMERACONTROLS_H
#define SCI_CAMERA_THIRDPERSONCAMERACONTROLS_H

#include <SCI/Camera/CameraControls.h>
#include <SCI/Camera/LookAt.h>


namespace SCI {

    class ThirdPersonCameraControls : public CameraControls
    {
    protected:

        float DistanceToCenter
        float AngleX, AngleY

        Vex3 up
        Vex3 DirectionToEye
        Vex3 Center

        Vex3 cs_x,cs_y,cs_z

        LookAt lat

        void _RecalcView()

    public:
        ThirdPersonCameraControls(startAngleX = 0.0f, startAngleY = 45.0f, startDistance = 40.0f, startCenter = Vex3(0,0,0), up = Vex3(0,1,0))
        ~ThirdPersonCameraControls(void)

        void Set(startAngleX = 0.0f, startAngleY = 45.0f, startDistance = 40.0f, startCenter = Vex3(0,0,0), up = Vex3(0,1,0))
        void SetCenter(Vex3 cen){ Center = cen; _RecalcView(); }

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
    }
}

#endif # SCI_CAMERA_THIRDPERSONCAMERACONTROLS_H
