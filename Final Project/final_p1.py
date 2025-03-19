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
            Describe the image with a description of the flower including petal shape color and size, the color and shape of the stamen,
            the appearance of the ovary and pistil, the shape, length and color of the penduncle, the leaf shape and color, 
            and the shape and color of the sepal.
            
            
            Definition of a petal:  in flowering plants, a sterile floral part that usually functions as a visually conspicuous 
            element of a flower. Petals are modified leaves and are often brightly coloured to attract specific pollinators to 
            the flower. Petals often come in multiples of three in monocots or in multiples of four or five in eudicots. 
            Many horticultural flowers, such as roses and peonies, have been bred to have multiple layers of petals, resulting
            in showy textured blooms.  Petals are located on the inner whorls of a flower, typically surrounded by the reproductive
            organs of the plant.

            
            Definition of a stamen:the male reproductive part of a flower. In all but a few extant angiosperms, the stamen consists 
            of a long slender stalk, the filament, with a two-lobed anther at the tip. The anther consists of four saclike structures
            (microsporangia) that produce pollen for pollination. Small secretory structures, called nectaries, are often found 
            at the base of the stamens; they provide food rewards for insect and bird pollinators. All the stamens of a flower are 
            collectively called the androecium. For a discussion of the female reproductive parts of a flower, see pistil.

            
            Definition of an ovary: enlarged basal portion of the pistil, the female organ of a flower. The ovary contains ovules, 
            which develop into seeds upon fertilization. The ovary itself will mature into a fruit, either dry or fleshy, enclosing 
            the seeds.

            
            Definition of a pistil:  the female reproductive part of a flower. The pistil, centrally located, typically consists of 
            a swollen base, the ovary, which contains the potential seeds, or ovules; a stalk, or style, arising from the ovary; and 
            a pollen-receptive tip, the stigma, variously shaped and often sticky. In pollination, compatible pollen grains land on 
            the stigma and then germinate, forming a pollen tube. The pollen tube grows down through the tissue of the style to 
            deposit sperm for the fertilization of the ovules in the ovary. Pistils in the collective sense form the gynoecium, in 
            distinction to the male reproductive parts, or androecium

            
            Definition of a penduncle: The receptacle is the axis (stem) to which the floral organs are attached. Floral organs are 
            attached either in a low continuous spiral, as is common among primitive angiosperms, or in alternating successive 
            whorls, as is found among most angiosperms.  The peduncle is the stalk of a flower or an inflorescence. When a flower 
            is borne singly, the internode between the receptacle and the bract (the last leaf, often modified and usually smaller 
            than the other leaves) is the peduncle. When the flowers are borne in an inflorescence, the peduncle is the internode 
            between the bract and the inflorescence; the internode between the receptacle of each flower and its underlying 
            bracteole is called a pedicel. Thus, in inflorescences, bracteole is the equivalent of bract, and pedicel is the 
            equivalent of peduncle.

            
            Defintition of a leaf: in botany, any usually flattened green outgrowth from the stem of a vascular plant. As the 
            primary sites of photosynthesis, leaves manufacture food for plants, which in turn ultimately nourish and sustain all 
            land animals. Botanically, leaves are an integral part of the stem system. They are attached by a continuous vascular 
            system to the rest of the plant so that free exchange of nutrients, water, and end products of photosynthesis 
            (oxygen and carbohydrates in particular) can be carried to its various parts. Leaves are initiated in the apical bud 
            (growing tip of a stem) along with the tissues of the stem itself. Certain organs that are superficially very different 
            from the usual green leaf are formed in the same manner and are actually modified leaves; among these are the sharp 
            spines of cacti, the needles of pines and other conifers, and the scales of an asparagus stalk or a lily bulb.

            
            Definition of a sepal: any of the outer parts of a flower that enclose and protect the unopened flower bud. The sepals 
            on a flower are collectively referred to as the calyx. They are sterile floral parts and may be either green or 
            leaflike or composed of petal-like tissue. From their base and along most of their length, sepals remain either 
            separate (aposepalous, or polysepalous) or marginally fused (synsepalous), forming a tube with terminal lobes or teeth. 
            The number of calyx lobes equals the number of fused (connate) sepals, and the number of sepals is usually the same as 
            the number of petals.

            Do not discribe the background, the flower should be the main focus of the description.
            Limmit word choice to contain only the most important details.
            If a detail is not present in the image, describe it as not present or non visable.

            """, 


			'images': ['./flower-2.jpg']
		}
	]
)

print(res['message']['content'])