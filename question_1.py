def molar_mass(molecule, atomic_weights):
    """
    Calculate the molar mass of a given molecule.
    
    Parameters:
    molecule (list of tuples): A list where each tuple contains an atomic symbol (str) and its count (int).
    atomic_weights (dict): A dictionary where keys are atomic symbols, and values are dictionaries containing 
                           the atomic name and atomic weight.
    
    Returns:
    float: The molar mass of the molecule if all elements are valid, otherwise None.
    """
    total_mass = 0.0
    
    for atom, count in molecule:
        if atom not in atomic_weights:
            return None  # Unknown atom found
        total_mass += count * atomic_weights[atom]['weight']
    
    return total_mass

atomic_weights = {
    'H': {'name': 'Hydrogen', 'weight': 1.00797},
    'He': {'name': 'Helium', 'weight': 4.00260},
    'C': {'name': 'Carbon', 'weight': 12.011},
    'O': {'name': 'Oxygen', 'weight': 15.9994}
}

if __name__ == "__main__":
    water = [('H', 2), ('O', 1)]
    acetic_acid = [('C', 1), ('H', 3), ('C', 1), ('O', 1), ('O', 1), ('H', 1)]
    unknown_molecule = [('X', 2), ('H', 1)]  # X is unknown

  


