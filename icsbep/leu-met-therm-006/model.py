import openmc
import numpy as np
import math
import os
from case_enum import case_enum

#############################################
# Benchmark:  LEU-MET-THERM-006 
# Cases:      1-30 
# Model by:   Nour Ali  
# Date:       26/08/2024
#############################################


class model:
    
    #left corner of the assembly
    xcorner=-40

    def __init__(self, case_info:case_enum, cross_section:str, w_unc=0, temperature=296, 
                 dense_unc= 0, relative_path= './case', batch=300, inactive=50, shannon=False, 
                 Tally=True, run=True) -> None:
        
        """
        case_info: case number given as case_enum object, EX: case_enum(1). \n
        cross_section: path to the cross section library used, EX: '/path/to/file/endfb-viii.0-hdf5/cross_sections.xml'.\n
        w_unc: uncertainty in critical water height.\n
        temperature: temperature of the model in kelvin.\n
        dense_unc: uncertainty in fuel density.\n
        relative_path: relative path to the directory where the xml files will be saved and case will be run. \n
        batch: number of batches.\n
        inactive: number of inactive batches.\n
        shannon: Bool, True to calculate the shannon entropy.\n
        Tally: Bool, True to calculate the tally.\n
        run: Bool, True to run the case.\n
        """
        
        self.case_info = case_info
        self.temp=temperature
        self.dense_unc=dense_unc
        self.r_path=relative_path
        self.cross_section=cross_section
        self.batch=batch
        self.inactive=inactive
        self.w_unc=w_unc

        self.setup()

        if run:
            if Tally:
                self.Get_Tally()
            if shannon:
                self.shannon_entropy()
                self.export_xml()

            self.run_model()

    def setup(self):
        openmc.config['cross_sections']= self.cross_section 
        self._init_global()
        self.material()
        self.fuel_cell()
        self.U_shaped_plates()
        self.beams()
        self.additional_plate()
        self.assembly()
        self.outer_box()
        self.root_geo()
        self.source_def()
        self.export_xml()
        self.setup_done=True
        
    def _init_global(self):

        # case Variables
        if self.case_info.additional_plate:
            self.w_height= openmc.ZPlane(0.4+self.case_info.w_h+self.w_unc)
        else:
            self.w_height= openmc.ZPlane(self.case_info.w_h + self.w_unc) 

        self.dx=self.case_info.pitch*math.cos(math.radians(30))
        self.dy=abs(self.case_info.pitch*math.sin(math.radians(30)))

        if self.case_info.additional_plate:
            self.z04=openmc.ZPlane(0.4)
            self.z59=openmc.ZPlane(59 + 0.4)
            self.z595=openmc.ZPlane(59 + 0.5 +0.4)
            self.z505=openmc.ZPlane(50 + 0.5 +0.4)
            self.z50=openmc.ZPlane(50.4)  
        else:
            self.z04=openmc.ZPlane(0)
            self.z59=openmc.ZPlane(59)
            self.z595=openmc.ZPlane(59 + 0.5)
            self.z505=openmc.ZPlane(50 + 0.5)
            self.z50=openmc.ZPlane(50)
        
        self.direc=self.r_path+str(self.case_info.c_no)
        self.abspath = os.path.abspath(self.direc)

        if not os.path.exists(self.abspath):
            os.mkdir(self.abspath)

        
    ## Materials     
    def fuel_mat(self):
        fuel=openmc.Material(temperature=self.temp)
        fuel.set_density('g/cc', 18.465 + self.dense_unc)
        fuel.add_nuclide('C0',9.2396E-04) #different cross section libraries accept C differently
        # fuel.add_nuclide('C12',9.137E-04)
        # fuel.add_nuclide('C13',1.024E-05)
        fuel.add_nuclide('Al27',2.8722E-04)

        Fe_ao=[5.47E-05,1.2633E-06,1.6812E-07]
        for i in range(0,3):
            fuel.add_nuclide('Fe'+str(56+i), Fe_ao[i])

        fuel.add_nuclide('Fe54', 3.4846E-06)

        U_ao=[7.0181E-06,7.5547E-04]
        for i in range(0,2):
            fuel.add_nuclide('U'+str(234+i), U_ao[i])

        fuel.add_nuclide('U238', 4.5866E-02)
        self.fuel = fuel

    def water_mat(self):
        self.water=openmc.Material(temperature=self.temp)
        self.water.set_density('g/cc', 0.99754)
        self.water.add_nuclide('H1',6.6682e-2)
        self.water.add_nuclide('H2',7.6693e-6)
        self.water.add_nuclide('O16',3.3265e-2)
        self.water.add_nuclide('O17', 1.2671e-5)
        self.water.add_s_alpha_beta('c_H_in_H2O')
        
    
    def air_mat(self):

        air=openmc.Material(temperature=self.temp)
        air.set_density('g/cc',0.0012)
        air.add_nuclide('O16',1.0568E-05)
        air.add_nuclide('O17',4.0258E-09)
        air.add_nuclide('N14',3.9349E-05)
        air.add_nuclide('N15',1.4375E-07 )
        self.air=air

    def steel_mat(self):
        steel=openmc.Material(temperature=self.temp)
        steel.set_density('g/cc', 7.9017)
        steel.add_nuclide('C0',5.5547e-4)
        # steel.add_nuclide('C12',5.493E-04)
        # steel.add_nuclide('C13',6.155E-06)
        steel.add_nuclide('Fe54', 4.9735e-3)
        fe_sao=[7.8073e-2,1.8031e-3,2.3995e-4]
        for i in range(0,3):
            steel.add_nuclide('Fe'+str(56+i), fe_sao[i])
        
        self.steel=steel
    
    def steelw_mat(self):
        steelw=openmc.Material(temperature=self.temp)
        steelw.set_density('g/cc', 6.4697)
        steelw.add_nuclide('C0', 1.0438E-04)
        # steelw.add_nuclide('C12',1.0322E-04)
        # steelw.add_nuclide('C13',1.1565E-06)
        nucl=['H1', 'H2', 'O16', 'O17', 'Si28', 'Si29', 'Si30', 'P31', 'S32', 'S33', 'S34',
            'S36', 'Cr50', 'Cr52','Cr53','Cr54', 'Mn55', 'Fe54', 'Fe56', 'Fe57', 'Fe58',
            'Ni58','Ni60', 'Ni61','Ni62', 'Ni64']
        aden=[1.0338E-02,1.1890E-06,5.1569E-03,1.9644E-06,1.3723E-03,6.9714E-05,4.6010E-05,
            5.3972E-05,3.7137E-05,2.9322E-07,1.6616E-06,3.9096E-09,6.2863E-04,1.2123E-02,
            1.3746E-03,3.4217E-04,1.5213E-03,3.0137E-03,4.7309E-02,1.0926E-03,1.4540E-04,
            4.8473E-04,1.8672E-04,8.1165E-06,2.5879E-05,6.5906E-06]
        for i in range(0,len(nucl)):
            steelw.add_nuclide(nucl[i],aden[i])

        steelw.add_s_alpha_beta('c_H_in_H2O')
        self.steelw=steelw

    def material(self):
        self.fuel_mat()
        self.water_mat()
        self.air_mat()
        self.steel_mat()
        self.steelw_mat()
        self.materials_file = openmc.Materials([self.fuel, self.water, 
                                                self.air, self.steel,self.steelw])
        self.colors={self.fuel: 'red', self.water:'blue',
                     self.air: 'green', self.steel:'grey', self.steelw:'lime'}

    
    ## Geometry 
    def fuel_cell(self):

        ## Surfaces
        ## Fuel
        ## Type 1
        inner_r1=openmc.ZCylinder(r=3.75)
        outer_r1=openmc.ZCylinder(r=4.85)

        #Type2
        inner_r2=openmc.ZCylinder(r=3.85)
        outer_r2=openmc.ZCylinder(r=4.75)

        #Disks
        disk_r=openmc.ZCylinder(r=4.85)

        ## Type 1
        fuel1c=openmc.Cell(name='f1c', fill=self.fuel, 
                           region=-outer_r1 & +inner_r1 & +self.z04 & -self.z59)
        disk1c=openmc.Cell(fill=self.steel, 
                           region=-disk_r & +self.z59 & -self.z595)
        #watrr inside fuel pin
        wa1=openmc.Cell(name='wain1', fill=self.water, 
                        region= -inner_r1 & +self.z04 & -self.w_height & -self.z59)
        #air inside fuel pin
        fair=openmc.Cell(fill=self.air, region=-inner_r1 & +self.w_height & -self.z59)

        pinwa=openmc.Cell(fill=self.water, 
                          region= +outer_r1 & +self.z04 & -self.w_height & -self.z595)
        pinair=openmc.Cell(fill=self.air, region= +outer_r1 & +self.w_height & -self.z595)

        self.f1=openmc.Universe(name='f1',cells=[fuel1c, disk1c, pinwa, pinair, fair, wa1])

        ## Type 2
        fuel2c=openmc.Cell(fill=self.fuel, 
                           region=-outer_r2 & +inner_r2 & +self.z04 & -self.z50)
        disk2c=openmc.Cell(fill=self.steel, 
                           region=-outer_r2 & +self.z50 & -self.z505)
        #water inside fuel pin
        wa2=openmc.Cell(fill=self.water, 
                        region= -inner_r2 & +self.z04 & -self.w_height & -self.z50)
        wa23=openmc.Cell(fill=self.water, 
                         region= -outer_r2 & +self.z505 & -self.w_height & -self.z595)
        #air inside fuel pin
        fair2=openmc.Cell(fill=self.air, region=-inner_r2 & +self.w_height &-self.z50)
        fair3=openmc.Cell(fill=self.air, 
                          region=-outer_r2 & +self.w_height & +self.z505 &-self.z595)

        pinwa2=openmc.Cell(fill=self.water, 
                           region= +outer_r2 & +self.z04 & -self.w_height & -self.z595)
        pinair2=openmc.Cell(fill=self.air, 
                            region= +outer_r2 & +self.w_height &-self.z595)
        self.f2=openmc.Universe(name='f2',cells=[fuel2c,disk2c,pinwa2,pinair2, fair2, fair3, wa2, wa23])

        ## Water pin
        pinw=openmc.Cell(fill=self.water, 
                         region=  +self.z04 & -self.w_height & -self.z595)
        pina=openmc.Cell(fill=self.air, region= +self.w_height & -self.z595)
        self.w3=openmc.Universe(name='w3',cells=[pinw,pina])

    def U_shaped_plates(self):

        ## U Plates

        top_plate=openmc.model.RectangularParallelepiped(xmin=0.3, xmax=9.7, 
                                                        ymin=0, ymax=100,
                                                        zmin=-0.2, zmax=0)

        left_pl=openmc.model.RectangularParallelepiped(xmin=0.3,xmax=0.5,
                                                    ymin=0, ymax=100,
                                                    zmin=-4, zmax=0)

        right_pl=openmc.model.RectangularParallelepiped(xmin=9.5, xmax=9.7,
                                                        ymin=0, ymax=100,
                                                        zmin=-4, zmax=0)

        whole_plate= -top_plate | -left_pl | -right_pl


        plate_bound= openmc.model.RectangularParallelepiped(xmin=0, xmax=(9.7+(0.6/2)),
                                                        ymin=0, ymax=100,
                                                        zmin=-4, zmax=0)

        plate_water = +top_plate | +left_pl | +right_pl

        uplate=openmc.Cell(fill=self.steel, region=whole_plate)
        uplate_w=openmc.Cell(fill= self.water, region= plate_water & -plate_bound)

        self.uplate0=openmc.Universe(cells=[uplate, uplate_w])
        self.uplate0c=openmc.Cell(fill=self.uplate0, region=-plate_bound)

        uplate_region_dict={}

        for i in range(0,5):
            uplate_region_dict['uplate'+str(i+1)]=openmc.model.RectangularParallelepiped(
                xmin=(i+1)*(9.4+0.6), xmax=(9.7+(0.6/2))+((i+1)*(9.4+0.6)),
                ymin=0, ymax=100,
                zmin=-4, zmax=0)
            uplate_region_dict['uplaten'+str(i+1)]=openmc.model.RectangularParallelepiped(
                xmin=-((i+1)*(9.4+0.6)), xmax=-((i+1)*(9.4+0.6))+(9.4+0.6),
                ymin=0, ymax=100,
                zmin=-4, zmax=0)


        self.uplate_dict={}
        for i in range(0,5):
            self.uplate_dict['uplate'+str(i+1)]=openmc.Cell(fill=self.uplate0, region=-uplate_region_dict['uplate'+str(i+1)])
            self.uplate_dict['uplate'+str(i+1)].translation=[(i+1)*(9.4+0.6),0,0]
            self.uplate_dict['uplaten'+str(i+1)]=openmc.Cell(fill=self.uplate0,region=-uplate_region_dict['uplaten'+str(i+1)])
            self.uplate_dict['uplaten'+str(i+1)].translation=[-(i+1)*(9.4+0.6),0,0]


        uplate_region_dict['uplaten'+str(5+1)]=openmc.model.RectangularParallelepiped(
            xmin=-((5+1)*(9.4+0.6)), xmax=-((5+1)*(9.4+0.6))+(9.4+0.6),
            ymin=0, ymax=100,
            zmin=-4, zmax=0)

        self.uplaten6=openmc.Cell(fill=self.uplate0, region=-uplate_region_dict['uplaten'+str(5+1)])
        self.uplaten6.translation=[-60,0,0]

    def beams(self):

        if self.case_info.additional_plate:
            zmin_outer=60.9
            zmax_outer=64.9
            zmin_inner=61.1
            zmax_inner=64.7
        else:
            zmin_outer=60.5
            zmax_outer=64.5
            zmin_inner=60.7
            zmax_inner=64.3

        
        ## Beams
        beam_outer = openmc.model.RectangularParallelepiped(xmin= model.xcorner-2, xmax=model.xcorner+2,
                                                            ymin= 0, ymax=100,
                                                            zmin=zmin_outer, zmax=zmax_outer)
        beam_inner=openmc.model.RectangularParallelepiped(xmin=model.xcorner-2+0.2, xmax=model.xcorner+2-0.2,
                                                        ymin=0, ymax=100,
                                                        zmin= zmin_inner, zmax=zmax_inner)
        whole_beam= +beam_inner & -beam_outer
        beam_cell=openmc.model.RectangularParallelepiped(xmin= model.xcorner-(self.case_info.pitch/2), 
                                                         xmax=model.xcorner+(self.case_info.pitch/2),
                                                     ymin=0, ymax=100,
                                                     zmin=zmin_outer, zmax=zmax_outer)

        beam=openmc.Cell(fill=self.steel, region=whole_beam)
        beam_cell_wa=openmc.Cell(fill=self.water, region= -beam_cell & +beam_outer  & -self.w_height)
        beam_wa_in=openmc.Cell(fill=self.water, region= -beam_inner  & -self.w_height)

        beam_cell_air=openmc.Cell(fill=self.air, region= -beam_cell & +beam_outer & +self.w_height)
        beam_air_in=openmc.Cell(fill=self.air, region= -beam_inner & +self.w_height)

        self.b1=openmc.Universe(cells=[beam, beam_cell_wa, beam_cell_air, beam_air_in, beam_wa_in])

        beam_region_dict={}
        self.beam_dict={}

        if self.case_info.lattice == 'rect':
            for i in range (0,self.case_info.beams_number_h):
                beam_region_dict['beam'+str(i)]=openmc.model.RectangularParallelepiped(
                    xmin=model.xcorner-(self.case_info.pitch/2) + ((i)*self.case_info.pitch), 
                    xmax = model.xcorner+(self.case_info.pitch/2) + ((i)*self.case_info.pitch),
                    ymin=0, ymax=100,
                    zmin=zmin_outer, zmax=zmax_outer
                )
                self.beam_dict['beam'+str(i)]=openmc.Cell(fill=self.b1, region=-beam_region_dict['beam'+str(i)])
                self.beam_dict['beam'+str(i)].translation=[(((i)*self.case_info.pitch)),0,0]

        if self.case_info.lattice == 'hex':
            for i in range (0,self.case_info.beams_number_h):
                beam_region_dict['beam'+str(i)]=openmc.model.RectangularParallelepiped(
                    xmin=model.xcorner-(self.case_info.pitch/2) + ((i)*self.dx), xmax = model.xcorner+(self.case_info.pitch/2) + ((i)*self.dx),
                    ymin=0, ymax=100,
                    zmin=zmin_outer, zmax=zmax_outer
                )
                self.beam_dict['beam'+str(i)]=openmc.Cell(fill=self.b1, region=-beam_region_dict['beam'+str(i)])
                self.beam_dict['beam'+str(i)].translation=[(((i)*self.dx)),0,0]


    def additional_plate(self):

        adplate=openmc.model.RectangularParallelepiped(xmin=-59.7, xmax=59.7,
                                                       ymin=0, ymax=100,
                                                       zmin=0, zmax=0.4)
        if self.case_info.additional_plate:
            self.addplate=openmc.Cell(fill=self.steelw, region=-adplate)
    

    def assembly(self):
        
        assembly_lat=self.case_info.assembly_lat
        
        translation = {'f1':self.f1, 'w3':self.w3, 'f2':self.f2}
        for i in range(0,len(assembly_lat)):
            for j in range(0, len(assembly_lat[i])):
                assembly_lat[i][j] = translation[assembly_lat[i][j]]


        if self.case_info.lattice == 'rect':
            rect_lat=openmc.RectLattice(name='Case30')

            rect_lat.pitch = (self.case_info.pitch, self.case_info.pitch)
            rect_lat.universes= assembly_lat


            rect_lat.lower_left=(model.xcorner-(self.case_info.pitch/2)-
                                self.case_info.pitch,10-(self.case_info.pitch/2)-self.case_info.pitch)


            self.assembly_length_h=(self.case_info.pitch*(self.case_info.beams_number_h+1))
            self.assembly_length_v=(self.case_info.pitch*(self.case_info.beams_number_v+1))

            assembly_bound=openmc.model.rectangular_prism(width=self.assembly_length_h, 
                                                        height=self.assembly_length_v, 
                                                        origin=(model.xcorner+(3*self.case_info.pitch),(3*self.case_info.pitch)+10), 
                                                        boundary_type='transmission') 

            self.assembly_cell=openmc.Cell(fill=rect_lat, region= assembly_bound & +self.z04 & -self.z595)
        
        if self.case_info.lattice == 'hex':
            dx1=self.case_info.diag*self.dx
            dy1=self.case_info.diag*self.dy + (self.case_info.vert*self.case_info.pitch)
            
            c_x=model.xcorner + dx1
            c_y=10 + dy1

            hex_lat = openmc.HexLattice()
            hex_lat.center = (c_x, c_y)
            hex_lat.pitch = (self.case_info.pitch,)
            hex_lat.outer = self.w3
            hex_lat.universes = assembly_lat

            self.dx_bound=2*dx1+3*self.case_info.pitch
            self.dy_bound=2*dy1+4*self.case_info.pitch
            
            lat_bound=openmc.model.rectangular_prism(width=self.dx_bound, height=self.dy_bound, 
                                        origin=(c_x, c_y), boundary_type='transmission') 


            self.assembly_cell=openmc.Cell(fill=hex_lat, region=lat_bound & +self.z04 & -self.z595)

    def outer_box(self):
        
        self.external=openmc.model.RectangularParallelepiped(xmin= -65, xmax=65,
                                                ymin= -20, ymax= 120,
                                                zmin=-10, zmax= 130)
        outw=openmc.Cell(fill= self.water, region= -self.external & -self.w_height)
        outa=openmc.Cell(fill=self.air, region= -self.external & +self.w_height)
        outbox=openmc.Universe(cells=[outw,outa])
        
        ##Zeroth Universe
        box_cell=openmc.Cell(fill=outbox, 
                             region= -self.external & ~self.assembly_cell.region 
                                & ~self.uplate0c.region
                                & ~self.uplaten6.region)
        
        if self.case_info.additional_plate:
            box_cell.region &= ~self.addplate.region
        
        for i in range(0,5):
            box_cell.region &= ~self.uplate_dict['uplate'+str(i+1)].region
            box_cell.region &= ~self.uplate_dict['uplaten'+str(i+1)].region
       
        for i in range(0, self.case_info.beams_number_h):
            box_cell.region &= ~self.beam_dict['beam' +str(i)].region                    
        
        U1=openmc.Universe(cells=[self.assembly_cell, box_cell, self.uplate0c, self.uplaten6])
        
        if self.case_info.additional_plate:
            U1.add_cell(self.addplate)
        
        for i in range(0,5):
            U1.add_cell(self.uplate_dict['uplate'+str(i+1)])
            U1.add_cell(self.uplate_dict['uplaten'+str(i+1)])
        
        for i in range(0,self.case_info.beams_number_h):
            U1.add_cell(self.beam_dict['beam'+str(i)])
        self.U1_cell=openmc.Cell(fill=U1, region= -self.external)
        
    def root_geo(self):
        self.outer_box()
        
        void=openmc.model.RectangularParallelepiped(xmin= -500, xmax=500,
                                                    ymin= -500, ymax= 500,
                                                    zmin=-500, zmax= 500, boundary_type='reflective')


        outer_void=openmc.Cell(region=+self.external & -void)
        U0=openmc.Universe(cells= [outer_void, self.U1_cell])

        self.geometry = openmc.Geometry(U0)
    
    def source_def(self):

        if self.case_info.lattice == 'hex':
            box_src = openmc.stats.Box([model.xcorner-self.case_info.pitch, 
                                        10-self.case_info.pitch, 0], 
                                    [model.xcorner-self.case_info.pitch+self.dx_bound,
                                      10-self.case_info.pitch+self.dy_bound, 60], 
                                    only_fissionable=True)
            src=openmc.IndependentSource(space=box_src)
            self.settings = openmc.Settings()
            self.settings.source = src
            self.settings.batches = self.batch
            self.settings.inactive = self.inactive
            self.settings.particles = 100000
        
        if self.case_info.lattice == 'rect':
            box_src=openmc.stats.Box([model.xcorner-(self.case_info.pitch/2)-self.case_info.pitch,
                                      10-(self.case_info.pitch/2)-self.case_info.pitch,0.4],
                                     [model.xcorner-(self.case_info.pitch/2)-self.case_info.pitch + self.assembly_length_h,
                                      10-(self.case_info.pitch/2)-self.case_info.pitch + self.assembly_length_v,59], 
                                      only_fissionable=True)
            src=openmc.IndependentSource(box_src)
            self.settings = openmc.Settings()
            self.settings.source = src
            self.settings.batches = 300
            self.settings.inactive = 50
            self.settings.particles = 100000


    def shannon_entropy(self):
        if self.case_info.lattice == 'rect':
            entropy_mesh = openmc.RegularMesh()
            entropy_mesh.lower_left = (model.xcorner-(self.case_info.pitch/2)-self.case_info.pitch,
                                       10-(self.case_info.pitch/2)-self.case_info.pitch,0.4)
            entropy_mesh.upper_right = (model.xcorner-(self.case_info.pitch/2)-self.case_info.pitch + self.assembly_length_h,
                                        10-(self.case_info.pitch/2)-self.case_info.pitch + self.assembly_length_v,
                                        60)
            entropy_mesh.dimension = (70, 70, 2)
            self.settings.entropy_mesh = entropy_mesh
        
        if self.case_info.lattice == 'hex':
            entropy_mesh = openmc.RegularMesh()
            entropy_mesh.lower_left = (model.xcorner-self.case_info.pitch,10-self.case_info.pitch,0)
            entropy_mesh.upper_right = (model.xcorner-self.case_info.pitch+self.dx_bound, 
                                        10-self.case_info.pitch+self.dy_bound,
                                        61)
            entropy_mesh.dimension = (70, 70, 2)
            self.settings.entropy_mesh = entropy_mesh
        

    def Get_Tally(self):
        
        tally=openmc.Tally()
        tally.scores = ['fission']
        energy_filter = openmc.EnergyFilter([0.0, 0.025, 0.625, 20e6])
        tally.filters = [energy_filter]
        self.tallies = openmc.Tallies([tally])
        self.tallies.export_to_xml(self.direc+'/tallies.xml')

    def export_xml(self):

        self.materials_file.export_to_xml(self.direc+'/materials.xml')
        self.geometry.export_to_xml(self.direc+'/geometry.xml')
        self.settings.export_to_xml(self.direc+'/settings.xml')

    def run_model(self):
        if self.setup_done:
            openmc.run(cwd=self.abspath, path_input=self.abspath)
    
    def statepoint(self):
        state=openmc.StatePoint(self.direc + f'/statepoint.{self.settings.batches}.h5')
        return state

    
   

