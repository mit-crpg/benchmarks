import openmc
from materials import materials
from surfaces import surfaces

###############################################################################
#                     Create a dictionary of all shared cells
###############################################################################

# Instantiate Cells
cells = {}
cells['UO2']                         = openmc.Cell(cell_id=1,  name='UO2')
cells['MOX 4.3%']                    = openmc.Cell(cell_id=2,  name='MOX 4.3%')
cells['MOX 7.0%']                    = openmc.Cell(cell_id=3,  name='MOX 7.0%')
cells['MOX 8.7%']                    = openmc.Cell(cell_id=4,  name='MOX 8.7%')
cells['Fission Chamber']             = openmc.Cell(cell_id=5,  name='Fission Chamber')
cells['Guide Tube']                  = openmc.Cell(cell_id=6,  name='Guide Tube')
cells['Reflector']                   = openmc.Cell(cell_id=7,  name='Reflector')
cells['Control Rod']                 = openmc.Cell(cell_id=8,  name='Control Rod')
cells['UO2 Moderator']               = openmc.Cell(cell_id=9,  name='UO2 Moderator')
cells['MOX 4.3% Moderator']          = openmc.Cell(cell_id=10, name='MOX 4.3% Moderator')
cells['MOX 7.0% Moderator']          = openmc.Cell(cell_id=11, name='MOX 7.0% Moderator')
cells['MOX 8.7% Moderator']          = openmc.Cell(cell_id=12, name='MOX 8.7% Moderator')
cells['Fission Chamber Moderator']   = openmc.Cell(cell_id=13, name='Fission Chamber Moderator')
cells['Guide Tube Moderator']        = openmc.Cell(cell_id=14, name='Guide Tube Moderator')
cells['Control Rod Moderator']       = openmc.Cell(cell_id=15, name='Control Rod Moderator')
cells['UO2 Unrodded Assembly']       = openmc.Cell(cell_id=16, name='UO2 Unrodded Assembly')
cells['UO2 Rodded Assembly']         = openmc.Cell(cell_id=17, name='UO2 Rodded Assembly')
cells['MOX Unrodded Assembly']       = openmc.Cell(cell_id=18, name='MOX Unrodded Assembly')
cells['MOX Rodded Assembly']         = openmc.Cell(cell_id=19, name='MOX Rodded Assembly')
cells['Reflector Unrodded Assembly'] = openmc.Cell(cell_id=20, name='Water Unrodded Assembly')
cells['Reflector Rodded Assembly']   = openmc.Cell(cell_id=21, name='Water Rodded Assembly')
cells['Core']                        = openmc.Cell(cell_id=22, name='Core')

# Use surface half-spaces to define regions
cells['UO2'].region                       = -surfaces['Pin Cell ZCylinder']
cells['MOX 4.3%'].region                  = -surfaces['Pin Cell ZCylinder']
cells['MOX 7.0%'].region                  = -surfaces['Pin Cell ZCylinder']
cells['MOX 8.7%'].region                  = -surfaces['Pin Cell ZCylinder']
cells['Fission Chamber'].region           = -surfaces['Pin Cell ZCylinder']
cells['Guide Tube'].region                = -surfaces['Pin Cell ZCylinder']
cells['Control Rod'].region               = -surfaces['Pin Cell ZCylinder']
cells['UO2 Moderator'].region             = +surfaces['Pin Cell ZCylinder']
cells['MOX 4.3% Moderator'].region        = +surfaces['Pin Cell ZCylinder']
cells['MOX 7.0% Moderator'].region        = +surfaces['Pin Cell ZCylinder']
cells['MOX 8.7% Moderator'].region        = +surfaces['Pin Cell ZCylinder']
cells['Fission Chamber Moderator'].region = +surfaces['Pin Cell ZCylinder']
cells['Guide Tube Moderator'].region      = +surfaces['Pin Cell ZCylinder']
cells['Control Rod Moderator'].region     = +surfaces['Pin Cell ZCylinder']

# Register Materials with Cells
cells['UO2'].fill                       = materials['UO2']
cells['MOX 4.3%'].fill                  = materials['MOX 4.3%']
cells['MOX 7.0%'].fill                  = materials['MOX 7.0%']
cells['MOX 8.7%'].fill                  = materials['MOX 8.7%']
cells['Fission Chamber'].fill           = materials['Fission Chamber']
cells['Guide Tube'].fill                = materials['Guide Tube']
cells['Control Rod'].fill               = materials['Control Rod']
cells['UO2 Moderator'].fill             = materials['Water']
cells['MOX 4.3% Moderator'].fill        = materials['Water']
cells['MOX 7.0% Moderator'].fill        = materials['Water']
cells['MOX 8.7% Moderator'].fill        = materials['Water']
cells['Fission Chamber Moderator'].fill = materials['Water']
cells['Guide Tube Moderator'].fill      = materials['Water']
cells['Control Rod Moderator'].fill     = materials['Water']
cells['Reflector'].fill                 = materials['Water']
