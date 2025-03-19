"""Using AI to describe an image and trying to get it to describe flowers in detail"""

#part one meta thingy megigger
"""
1. Cereate a main.py and subfolders with files with functions in them and import those funcitons in the main.py
2. recursion: looping wihtout loops, create a function which iterates a file link by line wihtout using while or for loops
3. integrate with AI create a simple commandline chat box which interferes with an llm allow it to work with immages."""

#importing Ollama
import ollama

#using the llava formula code and edditing the message content heavily
res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			
            #Botanical books are used for their definitions of flowers, petals, stamen, etc.
            #dictionaries uesed: Davesgarden.com, Britannica.com, 
            'content': """
            Describe the flower petals in detail.

            Petal definition:  in flowering plants, a sterile floral part that usually functions as a visually conspicuous 
            element of a flower. Petals are modified leaves and are often brightly coloured to attract specific pollinators to 
            the flower. Petals often come in multiples of three in monocots or in multiples of four or five in eudicots. 
            Many horticultural flowers, such as roses and peonies, have been bred to have multiple layers of petals, resulting
            in showy textured blooms.  Petals are located on the inner whorls of a flower, typically surrounded by the reproductive
            organs of the plant.

            some petal trigger words are the following: 'round', 'pointed', 'long', 'short', 'red', 'blue', 'yellow', 'small', 'large', 'smooth', 'rough', 'solid', 'striped', 'one', 'two', 'three',
    'oval', 'heart-shaped', 'lanceolate', 'oblong', 'white', 'pink', 'purple', 'orange', 'green', 'brown', 'black', 'tiny', 'huge', 'glossy', 
    'matte', 'velvety', 'fuzzy', 'hairy', 'spotted', 'blotched', 'mottled', 'speckled', 'translucent', 'opaque', 'thin', 'thick', 'narrow', 
    'broad', 'wavy', 'curled', 'flat', 'folded', 'crinkled', 'pleated', 'fringed', 'toothed', 'lobed', 'entire', 'undulate', 'serrated', 
    'dentate', 'crenate', 'incised', 'cleft', 'parted', 'divided', 'compound', 'simple', 'double', 'triple', 'quadruple', 'quintuple', 
    'clustered', 'solitary', 'paired', 'whorled', 'opposite', 'alternate', 'basal', 'cauline', 'terminal', 'axillary', 'radial', 'bilateral', 
    'symmetrical', 'asymmetrical', 'regular', 'irregular', 'fused', 'free', 'connate', 'adnate', 'deciduous', 'persistent', 'caducous', 
    'marcescent', 'papery', 'fleshy', 'succulent', 'membranous', 'leathery', 'coriaceous', 'chartaceous', 'scarious', 'glabrous', 'pubescent', 
    'tomentose', 'villous', 'pilose', 'hirsute', 'strigose', 'scabrous', 'rugose', 'bullate', 'pustulate', 'verrucose', 'areolate', 'reticulate', 
    'pitted', 'grooved', 'ridged', 'keeled', 'winged', 'appendaged', 'glandular', 'resinous', 'viscid', 'glutinous', 'sticky', 'waxy', 'powdery', 
    'mealy', 'crystalline', 'granular', 'fibrous', 'woody', 'herbaceous', 'annual', 'biennial', 'perennial', 'monocarpic', 'polycarpic', 
    'evergreen', 'deciduous', 'semi-evergreen', 'dormant', 'active', 'flowering', 'non-flowering', 'blooming', 'non-blooming', 'bud', 'blossom', 
    'inflorescence', 'floret', 'ray', 'disk', 'ligule', 'spikelet', 'spathe', 'bract', 'glume', 'lemma', 'palea', 'awn', 'rachilla', 'pedicel', 
    'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 'ovary', 'style', 'stigma', 'anther', 'filament', 
    'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 'tendril', 'climber', 'creeper', 'trailer', 'runner', 
    'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 'adventitious root', 'aerial root', 'prop root', 'buttress root', 
    'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 
    'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 
    'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 
    'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 
    'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 
    'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 
    'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 
    'bulb', 'corm', 'root', 'taproot', 'fibrous root', 'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 
    'nodule', 'lenticel', 'cork', 'bark', 'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 
    'guard cell', 'trichome', 'hair', 'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 
    'drupe', 'pome', 'capsule', 'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 
    'spike', 'raceme', 'panicle', 'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 
    'pappus', 'awn', 'glume', 'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 
    'stamen', 'pistil', 'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 
    'thorn', 'prickle', 'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 
    'fibrous root', 'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 
    'bark', 'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 
    'hair', 'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule',

        
            The description of the petals should be limited to the following and be concise:
                Describe the shape of the petals, round, pointed, long, short, etc.
                Describe the color of the petals, red, blue, yellow, etc.
                Describe the size of the petals, small, large, etc.
                Describe the texture of the petals, smooth, rough, etc.
                Describe the pattern of the petals, solid, striped, etc.
                Describe the number of petals, one, two, three, etc.

            Do not include any other information in the description of the image.
            """, 


			'images': ['./flower-2.jpg']
		}
	]
)

print(res['message']['content'])

#finding petal discriptors and printing them

#assign variables
petal_descriptors = []
petal_triggers = [
    'round', 'pointed', 'long', 'short', 'red', 'blue', 'yellow', 'small', 'large', 'smooth', 'rough', 'solid', 'striped', 'one', 'two', 'three',
    'oval', 'heart-shaped', 'lanceolate', 'oblong', 'white', 'pink', 'purple', 'orange', 'green', 'brown', 'black', 'tiny', 'huge', 'glossy', 
    'matte', 'velvety', 'fuzzy', 'hairy', 'spotted', 'blotched', 'mottled', 'speckled', 'translucent', 'opaque', 'thin', 'thick', 'narrow', 
    'broad', 'wavy', 'curled', 'flat', 'folded', 'crinkled', 'pleated', 'fringed', 'toothed', 'lobed', 'entire', 'undulate', 'serrated', 
    'dentate', 'crenate', 'incised', 'cleft', 'parted', 'divided', 'compound', 'simple', 'double', 'triple', 'quadruple', 'quintuple', 
    'clustered', 'solitary', 'paired', 'whorled', 'opposite', 'alternate', 'basal', 'cauline', 'terminal', 'axillary', 'radial', 'bilateral', 
    'symmetrical', 'asymmetrical', 'regular', 'irregular', 'fused', 'free', 'connate', 'adnate', 'deciduous', 'persistent', 'caducous', 
    'marcescent', 'papery', 'fleshy', 'succulent', 'membranous', 'leathery', 'coriaceous', 'chartaceous', 'scarious', 'glabrous', 'pubescent', 
    'tomentose', 'villous', 'pilose', 'hirsute', 'strigose', 'scabrous', 'rugose', 'bullate', 'pustulate', 'verrucose', 'areolate', 'reticulate', 
    'pitted', 'grooved', 'ridged', 'keeled', 'winged', 'appendaged', 'glandular', 'resinous', 'viscid', 'glutinous', 'sticky', 'waxy', 'powdery', 
    'mealy', 'crystalline', 'granular', 'fibrous', 'woody', 'herbaceous', 'annual', 'biennial', 'perennial', 'monocarpic', 'polycarpic', 
    'evergreen', 'deciduous', 'semi-evergreen', 'dormant', 'active', 'flowering', 'non-flowering', 'blooming', 'non-blooming', 'bud', 'blossom', 
    'inflorescence', 'floret', 'ray', 'disk', 'ligule', 'spikelet', 'spathe', 'bract', 'glume', 'lemma', 'palea', 'awn', 'rachilla', 'pedicel', 
    'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 'ovary', 'style', 'stigma', 'anther', 'filament', 
    'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 'tendril', 'climber', 'creeper', 'trailer', 'runner', 
    'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 'adventitious root', 'aerial root', 'prop root', 'buttress root', 
    'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 
    'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 
    'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 
    'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 
    'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 
    'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 
    'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 
    'bulb', 'corm', 'root', 'taproot', 'fibrous root', 'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 
    'nodule', 'lenticel', 'cork', 'bark', 'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 
    'guard cell', 'trichome', 'hair', 'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 
    'drupe', 'pome', 'capsule', 'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 
    'spike', 'raceme', 'panicle', 'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 
    'pappus', 'awn', 'glume', 'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 
    'stamen', 'pistil', 'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 
    'thorn', 'prickle', 'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 
    'fibrous root', 'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 
    'bark', 'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 
    'hair', 'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule', 'lenticel', 'cork', 'bark', 
    'periderm', 'phloem', 'xylem', 'cambium', 'pith', 'medulla', 'cortex', 'epidermis', 'cuticle', 'stoma', 'guard cell', 'trichome', 'hair', 
    'scale', 'gland', 'resin', 'latex', 'gum', 'sap', 'nectar', 'pollen', 'spore', 'seed', 'fruit', 'berry', 'drupe', 'pome', 'capsule', 
    'legume', 'pod', 'follicle', 'samara', 'nut', 'achene', 'caryopsis', 'grain', 'cone', 'strobilus', 'catkin', 'spike', 'raceme', 'panicle', 
    'umbel', 'corymb', 'cyme', 'head', 'cluster', 'spadix', 'spathe', 'bract', 'involucre', 'phyllary', 'chaff', 'pappus', 'awn', 'glume', 
    'lemma', 'palea', 'rachilla', 'pedicel', 'peduncle', 'receptacle', 'calyx', 'corolla', 'androecium', 'gynoecium', 'stamen', 'pistil', 
    'ovary', 'style', 'stigma', 'anther', 'filament', 'nectary', 'spur', 'gland', 'hair', 'trichome', 'scale', 'spine', 'thorn', 'prickle', 
    'tendril', 'climber', 'creeper', 'trailer', 'runner', 'stolon', 'rhizome', 'tuber', 'bulb', 'corm', 'root', 'taproot', 'fibrous root', 
    'adventitious root', 'aerial root', 'prop root', 'buttress root', 'haustorium', 'mycorrhiza', 'nodule'
]
words = res['message']['content'].split()
index = 0

#while loop to keep it going untill there are no more trigger words
while index < len(words): 
    word = words[index]
    if word in petal_triggers:
        petal_descriptors.append(word)
    index += 1
print()
print("Petal Descriptors: ", petal_descriptors)

#assigning numbers to the petal descriptors