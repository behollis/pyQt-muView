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

#ifndef SCI_CAMERA_FRUSTUMPROJECTION_H
#define SCI_CAMERA_FRUSTUMPROJECTION_H

#include <SCI/Camera/Projection.h>

namespace SCI {

    class FrustumProjection : public Projection {

        Q_OBJECT

    public slots:
        void SetHFOV(double fov){ Set(hfov,fov,hither,yon); }
        void SetVFOV(double fov){ Set(fov,vfov,hither,yon); }
        void SetHither(double znear){ Set(hfov,vfov,znear,yon); }
        void SetYon(double zfar){ Set(hfov,vfov,hither,zfar); }

    protected:
        SCI.Mat4 proj, iproj

        float hfov,vfov,hither,yon

        void _Set(float left, right, bottom, top, znear, zfar)
    public:
        FrustumProjection(hfov = 45.0f, vfov = 45.0f, znear = 1.0f, zfar = 100.0f)
        FrustumProjection(float hfov, w, h, znear, zfar)
        ~FrustumProjection(void)

        void Set(float hfov, w, h, znear, zfar)
        void Set(float hfov, vfov, znear, zfar)

        #void SetHither(float znear){ Set(hfov,vfov,znear,yon); }
        #void SetYon(float zfar){ Set(hfov,vfov,hither,zfar); }

        virtual void glSetProjection(loadIdent = True)

        bool inFrustum(SCI.Vex3 p3d)

        virtual SCI.Mat4 GetMatrix()        {    return proj;    }
        virtual SCI.Mat4 GetInverseMatrix()    {    return iproj;    }

        float GetHFOV(){    return hfov;    }
        float GetVFOV(){    return vfov;    }
        float GetHither(){    return hither;    }
        float GetYon(){        return yon;        }

        FrustumProjection& operator=(FrustumProjection& other){
            Set(other.hfov,other.vfov,other.hither,other.yon)
            return (*self)
        }

        void glDrawFrustumVisualization()

        bool Save( char * fname)
        bool Load( char * fname)
    }
}

#endif # SCI_CAMERA_FRUSTUMPROJECTION_H
