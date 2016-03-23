import openmc

###############################################################################
#                     Create a dictionary of all shared cells
###############################################################################

# Create a dictionary to store the surfaces
surfaces = {}

# Instantiate Pin Cell ZCylinder surface
surfaces['Pin Cell ZCylinder'] = openmc.ZCylinder(surface_id=1, x0=0, y0=0, R=0.54, name='Pin Cell ZCylinder')
surfaces['Core x-min']       = openmc.XPlane(surface_id=2, x0=-32.13, name='Core x-min')
surfaces['Core x-max']       = openmc.XPlane(surface_id=3, x0= 32.13, name='Core x-max')
surfaces['Core y-min']       = openmc.YPlane(surface_id=4, y0=-32.13, name='Core y-min')
surfaces['Core y-max']       = openmc.YPlane(surface_id=5, y0= 32.13, name='Core y-max')
surfaces['Small Core z-min'] = openmc.ZPlane(surface_id=6, z0=-32.13, name='Small Core z-min')
surfaces['Small Core z-max'] = openmc.ZPlane(surface_id=7, z0= 32.13, name='Small Core z-max')
surfaces['Big Core z-min']   = openmc.ZPlane(surface_id=8, z0=-107.1, name='Big Core z-min')
surfaces['Big Core z-max']   = openmc.ZPlane(surface_id=9, z0= 107.1, name='Big Core z-max')
surfaces['Pin x-min']        = openmc.XPlane(surface_id=10, x0=-0.63, name='Pin x-min')
surfaces['Pin x-max']        = openmc.XPlane(surface_id=11, x0=+0.63, name='Pin x-max')
surfaces['Pin y-min']        = openmc.YPlane(surface_id=12, y0=-0.63, name='Pin y-min')
surfaces['Pin y-max']        = openmc.YPlane(surface_id=13, y0=+0.63, name='Pin y-max')

surfaces['Core x-max'].boundary_type       = 'vacuum'
surfaces['Core y-min'].boundary_type       = 'vacuum'
surfaces['Core y-max'].boundary_type       = 'reflective'
surfaces['Small Core z-min'].boundary_type = 'reflective'
surfaces['Small Core z-max'].boundary_type = 'vacuum'
surfaces['Big Core z-min'].boundary_type   = 'reflective'
surfaces['Big Core z-max'].boundary_type   = 'vacuum'
surfaces['Pin x-min'].boundary_type        = 'reflective'
surfaces['Pin x-max'].boundary_type        = 'reflective'
surfaces['Pin y-min'].boundary_type        = 'reflective'
surfaces['Pin y-max'].boundary_type        = 'reflective'
surfaces['Core x-min'].boundary_type       = 'reflective'
