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

#ifndef SCI_CAMERA_ORTHOPROJECTION_H
#define SCI_CAMERA_ORTHOPROJECTION_H

#include <SCI/Camera/Projection.h>

namespace SCI {

    class OrthoProjection :    public Projection {

        Q_OBJECT

    protected:
        float left,right
        float bottom,top
        float znear,zfar

        SCI.Mat4 proj
        SCI.Mat4 iproj

    public:
        OrthoProjection(left = -1, right = 1, bottom = -1, top = 1, znear= -1, zfar = 1)
        ~OrthoProjection(void)

        void Set(float left, right, bottom, top, znear, zfar)

        virtual void glSetProjection(loadIdent = True)

        virtual SCI.Mat4 GetMatrix()        {    return proj;    }
        virtual SCI.Mat4 GetInverseMatrix()    {    return iproj;    }
    }
}

#endif # SCI_CAMERA_ORTHOPROJECTION_H
