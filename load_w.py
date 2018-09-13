from cosmosis.datablock import option_section
import numpy as np

def setup(options):
    """
    This function is run once at the start of any analysis.
    """
    # Read the name of the w file to use from the parameter file
    w_filename = options[option_section, 'w_filename']
    
    # Load that file as text columns
    w_data = np.loadtxt(w_filename).T

    #  Assume that first two columns are z, w(z)
    z = w_data[0]
    w = w_data[1]

    # Compute 
    a = 1./(1.+z)

    # CAMB wants 
    if a[1]<a[0]:
        z = z[::-1]
        a = a[::-1]
        w = w[::-1]

    # Return all these to the 
    return {'z': z, 'w':w, 'a':a}

def execute(block, config):
    """
    This function is run once per cosmological parameter set.
    For the test sampler that's still just once, though
    """

    # Save our a and w values to the block
    section = 'de_equation_of_state'
    block[section, 'a'] = config['a']
    block[section, 'w'] = config['w']

    # No errors
    return 0