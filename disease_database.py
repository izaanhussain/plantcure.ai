"""
Disease Information Database
Contains comprehensive information about plant diseases
"""

class DiseaseDatabase:
    """Database of plant disease information"""
    
    def __init__(self):
        """Initialize disease database with comprehensive information"""
        self.diseases = {
            # Apple diseases
            'Apple___Apple_scab': {
                'name': 'Apple Scab',
                'scientific_name': 'Venturia inaequalis',
                'description': 'Apple scab is a fungal disease that affects apples, crabapples, and other members of the rose family. It causes dark, scabby lesions on leaves, fruit, and sometimes young twigs.',
                'symptoms': 'Olive-green to black spots on leaves and fruit; velvety lesions; premature leaf drop; fruit deformation.',
                'cause': 'Fungal infection (Venturia inaequalis) that thrives in cool, wet conditions.',
                'treatment_organic': 'Apply sulfur or copper-based fungicides; remove fallen leaves; improve air circulation; plant resistant varieties.',
                'treatment_chemical': 'Apply fungicides containing captan, myclobutanil, or trifloxystrobin at bud break and throughout the season.',
                'prevention': 'Plant resistant varieties; prune for air circulation; remove fallen leaves; avoid overhead irrigation.',
                'difficulty': 'Moderate'
            },
            'Apple___Black_rot': {
                'name': 'Apple Black Rot',
                'scientific_name': 'Botryosphaeria obtusa',
                'description': 'Black rot is a fungal disease that can affect leaves, fruit, and wood of apple trees. It is most serious in warm, humid regions.',
                'symptoms': 'Purple-bordered black spots on leaves; black, sunken lesions on fruit with concentric rings; cankers on branches.',
                'cause': 'Fungal infection (Botryosphaeria obtusa) that overwinters in mummified fruit and cankers.',
                'treatment_organic': 'Remove mummified fruit and cankers; apply sulfur sprays; maintain tree vigor.',
                'treatment_chemical': 'Apply fungicides such as captan, thiophanate-methyl, or myclobutanil during the growing season.',
                'prevention': 'Remove and destroy infected fruit and wood; prune for air circulation; avoid overhead irrigation.',
                'difficulty': 'Moderate to High'
            },
            'Apple___Cedar_apple_rust': {
                'name': 'Cedar Apple Rust',
                'scientific_name': 'Gymnosporangium juniperi-virginianae',
                'description': 'Cedar apple rust is a fungal disease that requires two hosts: apple/crabapple and eastern red cedar/juniper. It causes bright orange spots on leaves and fruit.',
                'symptoms': 'Bright orange to yellow spots on upper leaf surface; cylindrical spore horns on cedar trees; fruit deformation.',
                'cause': 'Fungal infection that alternates between apple and cedar/juniper hosts.',
                'treatment_organic': 'Remove nearby cedar trees if possible; apply sulfur fungicides; plant resistant varieties.',
                'treatment_chemical': 'Apply fungicides containing myclobutanil, propiconazole, or mancozeb before and during bloom.',
                'prevention': 'Avoid planting apples near cedar trees; choose resistant varieties; apply preventive fungicides.',
                'difficulty': 'Moderate'
            },
            'Apple___healthy': {
                'name': 'Healthy Apple',
                'scientific_name': 'Malus domestica',
                'description': 'Healthy apple tree with no visible disease symptoms. Proper care includes regular watering, fertilization, and pest monitoring.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; monitor for pests and diseases.',
                'treatment_chemical': 'No chemical treatment needed for healthy trees.',
                'prevention': 'Maintain good cultural practices; regular monitoring; proper pruning and fertilization.',
                'difficulty': 'N/A'
            },
            
            # Blueberry
            'Blueberry___healthy': {
                'name': 'Healthy Blueberry',
                'scientific_name': 'Vaccinium corymbosum',
                'description': 'Healthy blueberry plant with no visible disease symptoms. Blueberries require acidic soil and consistent moisture.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; ensure soil pH is acidic (4.5-5.5).',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Maintain proper soil pH; adequate irrigation; regular pruning.',
                'difficulty': 'N/A'
            },
            
            # Cherry diseases
            'Cherry_(including_sour)___Powdery_mildew': {
                'name': 'Cherry Powdery Mildew',
                'scientific_name': 'Podosphaera clandestina',
                'description': 'Powdery mildew is a fungal disease that creates a white, powdery coating on cherry leaves, shoots, and fruit.',
                'symptoms': 'White powdery coating on leaves and shoots; leaf distortion; fruit cracking and russeting.',
                'cause': 'Fungal infection that thrives in warm, dry conditions with high humidity.',
                'treatment_organic': 'Apply sulfur or neem oil; improve air circulation; remove infected tissue.',
                'treatment_chemical': 'Apply fungicides such as myclobutanil, trifloxystrobin, or propiconazole.',
                'prevention': 'Plant resistant varieties; prune for air circulation; avoid excessive nitrogen.',
                'difficulty': 'Moderate'
            },
            'Cherry_(including_sour)___healthy': {
                'name': 'Healthy Cherry',
                'scientific_name': 'Prunus avium',
                'description': 'Healthy cherry tree with no visible disease symptoms. Cherries require well-draining soil and full sun.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; monitor for pests and diseases.',
                'treatment_chemical': 'No chemical treatment needed for healthy trees.',
                'prevention': 'Regular monitoring; proper pruning; adequate irrigation.',
                'difficulty': 'N/A'
            },
            
            # Corn diseases
            'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
                'name': 'Corn Gray Leaf Spot',
                'scientific_name': 'Cercospora zeae-maydis',
                'description': 'Gray leaf spot is a fungal disease of corn that causes rectangular gray lesions on leaves, reducing photosynthesis and yield.',
                'symptoms': 'Rectangular, gray to tan lesions on leaves; lesions restricted by leaf veins; premature leaf death.',
                'cause': 'Fungal infection that overwinds in crop residue; favored by warm, humid weather.',
                'treatment_organic': 'Rotate crops; reduce residue; plant resistant hybrids; ensure proper plant spacing.',
                'treatment_chemical': 'Apply fungicides such as pyraclostrobin, azoxystrobin, or propiconazole at early signs.',
                'prevention': 'Crop rotation; tillage to reduce residue; resistant hybrids; proper plant density.',
                'difficulty': 'Moderate'
            },
            'Corn_(maize)___Common_rust_': {
                'name': 'Corn Common Rust',
                'scientific_name': 'Puccinia sorghi',
                'description': 'Common rust is a fungal disease that produces reddish-brown pustules on corn leaves, potentially reducing yield.',
                'symptoms': 'Reddish-brown, oval pustules on leaves; leaf tissue tearing around pustules; premature senescence.',
                'cause': 'Fungal infection that spreads via wind-blown spores; favored by cool, humid conditions.',
                'treatment_organic': 'Plant resistant hybrids; rotate crops; avoid late planting in prone areas.',
                'treatment_chemical': 'Apply fungicides such as azoxystrobin, pyraclostrobin, or propiconazole preventively.',
                'prevention': 'Resistant hybrids; crop rotation; timely planting; avoid overhead irrigation.',
                'difficulty': 'Low to Moderate'
            },
            'Corn_(maize)___Northern_Leaf_Blight': {
                'name': 'Corn Northern Leaf Blight',
                'scientific_name': 'Exserohilum turcicum',
                'description': 'Northern leaf blight is a fungal disease causing long, cigar-shaped lesions on corn leaves, significantly reducing yield.',
                'symptoms': 'Long, cigar-shaped gray-green lesions on leaves; lesions turn tan with dark borders; leaf blighting.',
                'cause': 'Fungal infection that overwinters in residue; favored by cool, wet weather.',
                'treatment_organic': 'Rotate crops; reduce residue; plant resistant hybrids; till infected residue.',
                'treatment_chemical': 'Apply fungicides such as azoxystrobin, pyraclostrobin, or mixed fungicide products.',
                'prevention': 'Resistant hybrids; crop rotation; residue management; proper plant density.',
                'difficulty': 'Moderate to High'
            },
            'Corn_(maize)___healthy': {
                'name': 'Healthy Corn',
                'scientific_name': 'Zea mays',
                'description': 'Healthy corn plant with no visible disease symptoms. Corn requires adequate nitrogen and consistent moisture.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal ear development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; ensure adequate nutrition.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Proper fertilization; irrigation; crop rotation; pest monitoring.',
                'difficulty': 'N/A'
            },
            
            # Grape diseases
            'Grape___Black_rot': {
                'name': 'Grape Black Rot',
                'scientific_name': 'Guignardia bidwellii',
                'description': 'Black rot is a serious fungal disease of grapes that causes brown circular lesions on leaves and fruit rot.',
                'symptoms': 'Circular brown spots on leaves with dark borders; small reddish-brown spots on fruit that expand and rot.',
                'cause': 'Fungal infection that overwinters in mummified fruit and cankers.',
                'treatment_organic': 'Remove mummified fruit and infected tissue; apply sulfur; improve air circulation.',
                'treatment_chemical': 'Apply fungicides such as mancozeb, captan, myclobutanil, or azoxystrobin regularly.',
                'prevention': 'Remove infected material; prune for air circulation; avoid overhead irrigation.',
                'difficulty': 'High'
            },
            'Grape___Esca_(Black_Measles)': {
                'name': 'Grape Esca (Black Measles)',
                'scientific_name': 'Phaeomoniella chlamydospora',
                'description': 'Esca is a complex fungal disease of grapevines causing leaf speckling, trunk damage, and eventual vine decline.',
                'symptoms': 'Tiger-striped leaves with yellow/brown areas; fruit blackening; trunk cankers; vine decline.',
                'cause': 'Fungal infection through pruning wounds; multiple fungi involved.',
                'treatment_organic': 'Remove infected wood; protect pruning wounds; maintain vine vigor.',
                'treatment_chemical': 'Apply fungicide pastes to pruning wounds; no cure for established infections.',
                'prevention': 'Protect pruning wounds; avoid pruning during wet conditions; remove infected wood.',
                'difficulty': 'Very High'
            },
            'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
                'name': 'Grape Leaf Blight',
                'scientific_name': 'Pseudocercospora vitis',
                'description': 'Leaf blight is a fungal disease causing reddish-brown lesions on grape leaves, leading to premature defoliation.',
                'symptoms': 'Reddish-brown circular lesions on leaves; yellow halos around lesions; premature leaf drop.',
                'cause': 'Fungal infection favored by warm, wet conditions.',
                'treatment_organic': 'Remove infected leaves; improve air circulation; apply sulfur or copper.',
                'treatment_chemical': 'Apply fungicides such as mancozeb, captan, or azoxystrobin preventively.',
                'prevention': 'Prune for air circulation; avoid overhead irrigation; remove leaf debris.',
                'difficulty': 'Moderate'
            },
            'Grape___healthy': {
                'name': 'Healthy Grape',
                'scientific_name': 'Vitis vinifera',
                'description': 'Healthy grapevine with no visible disease symptoms. Grapes require full sun and well-draining soil.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper pruning and training.',
                'treatment_chemical': 'No chemical treatment needed for healthy vines.',
                'prevention': 'Regular monitoring; proper canopy management; adequate irrigation.',
                'difficulty': 'N/A'
            },
            
            # Orange
            'Orange___Haunglongbing_(Citrus_greening)': {
                'name': 'Citrus Greening (HLB)',
                'scientific_name': 'Candidatus Liberibacter asiaticus',
                'description': 'Huanglongbing (HLB) or citrus greening is a devastating bacterial disease spread by citrus psyllids, causing fruit distortion and tree decline.',
                'symptoms': 'Asymmetric, blotchy mottling of leaves; yellow shoots; small, lopsided, bitter fruit; tree decline.',
                'cause': 'Bacterial infection spread by Asian citrus psyllid; incurable in established trees.',
                'treatment_organic': 'Remove infected trees; control psyllid populations with beneficial insects; maintain tree health.',
                'treatment_chemical': 'Apply systemic insecticides to control psyllids; antibiotic treatments (limited efficacy).',
                'prevention': 'Monitor for psyllids; use certified disease-free trees; remove infected trees promptly.',
                'difficulty': 'Very High'
            },
            
            # Peach diseases
            'Peach___Bacterial_spot': {
                'name': 'Peach Bacterial Spot',
                'scientific_name': 'Xanthomonas arboricola pv. pruni',
                'description': 'Bacterial spot is a serious disease of stone fruits causing small, water-soaked lesions on leaves, fruit, and twigs.',
                'symptoms': 'Small, angular water-soaked spots on leaves; brown, corky lesions on fruit; twig cankers.',
                'cause': 'Bacterial infection that spreads via rain and wind; favored by warm, wet conditions.',
                'treatment_organic': 'Apply copper sprays; remove infected tissue; improve air circulation.',
                'treatment_chemical': 'Apply copper-containing bactericides or oxytetracycline during dormancy and growing season.',
                'prevention': 'Plant resistant varieties; avoid overhead irrigation; apply preventive copper sprays.',
                'difficulty': 'High'
            },
            'Peach___healthy': {
                'name': 'Healthy Peach',
                'scientific_name': 'Prunus persica',
                'description': 'Healthy peach tree with no visible disease symptoms. Peaches require well-draining soil and chill hours.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper thinning and pruning.',
                'treatment_chemical': 'No chemical treatment needed for healthy trees.',
                'prevention': 'Regular monitoring; proper pruning; adequate irrigation and nutrition.',
                'difficulty': 'N/A'
            },
            
            # Pepper diseases
            'Pepper,_bell___Bacterial_spot': {
                'name': 'Pepper Bacterial Spot',
                'scientific_name': 'Xanthomonas euvesicatoria',
                'description': 'Bacterial spot causes water-soaked lesions on pepper leaves, stems, and fruit, reducing yield and fruit quality.',
                'symptoms': 'Small, water-soaked spots on leaves; yellow halos; raised scabby lesions on fruit.',
                'cause': 'Bacterial infection spread by water splash, tools, and insects; favored by warm, wet conditions.',
                'treatment_organic': 'Apply copper sprays; remove infected plant debris; use disease-free seeds.',
                'treatment_chemical': 'Apply copper-containing bactericides or streptomycin (where registered).',
                'prevention': 'Use disease-free seeds and transplants; crop rotation; avoid overhead irrigation.',
                'difficulty': 'Moderate to High'
            },
            'Pepper,_bell___healthy': {
                'name': 'Healthy Bell Pepper',
                'scientific_name': 'Capsicum annuum',
                'description': 'Healthy pepper plant with no visible disease symptoms. Peppers require warm temperatures and consistent moisture.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper staking and pruning.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Regular monitoring; proper spacing; adequate irrigation and fertilization.',
                'difficulty': 'N/A'
            },
            
            # Potato diseases
            'Potato___Early_blight': {
                'name': 'Potato Early Blight',
                'scientific_name': 'Alternaria solani',
                'description': 'Early blight is a fungal disease causing dark concentric lesions on potato leaves, reducing yield and tuber quality.',
                'symptoms': 'Dark brown lesions with concentric rings on older leaves; yellowing; tuber lesions.',
                'cause': 'Fungal infection that overwinters in soil and plant debris; favored by warm, humid conditions.',
                'treatment_organic': 'Remove infected tissue; apply copper fungicides; maintain plant vigor.',
                'treatment_chemical': 'Apply fungicides such as chlorothalonil, mancozeb, or azoxystrobin preventively.',
                'prevention': 'Crop rotation; resistant varieties; avoid overhead irrigation; proper plant spacing.',
                'difficulty': 'Moderate'
            },
            'Potato___Late_blight': {
                'name': 'Potato Late Blight',
                'scientific_name': 'Phytophthora infestans',
                'description': 'Late blight is a devastating fungal disease that caused the Irish potato famine; it rapidly kills potato foliage and tubers.',
                'symptoms': 'Water-soaked lesions on leaves; white fungal growth on undersides; black, firm tuber rot.',
                'cause': 'Fungal-like pathogen that spreads rapidly in cool, wet conditions.',
                'treatment_organic': 'Remove infected plants immediately; apply copper fungicides; destroy crop debris.',
                'treatment_chemical': 'Apply fungicides such as mancozeb, chlorothalonil, or metalaxyl preventively.',
                'prevention': 'Plant certified seed potatoes; avoid planting near tomatoes; eliminate volunteer plants.',
                'difficulty': 'Very High'
            },
            'Potato___healthy': {
                'name': 'Healthy Potato',
                'scientific_name': 'Solanum tuberosum',
                'description': 'Healthy potato plant with no visible disease symptoms. Potatoes require well-draining soil and hilling.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal tuber development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper hilling and pest control.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Use certified seed potatoes; proper rotation; adequate irrigation.',
                'difficulty': 'N/A'
            },
            
            # Raspberry
            'Raspberry___healthy': {
                'name': 'Healthy Raspberry',
                'scientific_name': 'Rubus idaeus',
                'description': 'Healthy raspberry plant with no visible disease symptoms. Raspberries require well-draining soil and support.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper trellising and pruning.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Regular monitoring; proper pruning; adequate irrigation and nutrition.',
                'difficulty': 'N/A'
            },
            
            # Soybean
            'Soybean___healthy': {
                'name': 'Healthy Soybean',
                'scientific_name': 'Glycine max',
                'description': 'Healthy soybean plant with no visible disease symptoms. Soybeans fix nitrogen and require well-draining soil.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal pod development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper inoculation if needed.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Proper rotation; adequate irrigation; pest monitoring.',
                'difficulty': 'N/A'
            },
            
            # Squash
            'Squash___Powdery_mildew': {
                'name': 'Squash Powdery Mildew',
                'scientific_name': 'Podosphaera xanthii',
                'description': 'Powdery mildew is a common fungal disease of squash causing white powdery coating on leaves, reducing yield.',
                'symptoms': 'White powdery coating on leaves; yellowing; leaf curling; reduced fruit production.',
                'cause': 'Fungal infection favored by warm, dry conditions with high humidity.',
                'treatment_organic': 'Apply sulfur or neem oil; remove infected leaves; improve air circulation.',
                'treatment_chemical': 'Apply fungicides such as myclobutanil, trifloxystrobin, or propiconazole.',
                'prevention': 'Plant resistant varieties; space plants properly; avoid overhead irrigation.',
                'difficulty': 'Low to Moderate'
            },
            
            # Strawberry diseases
            'Strawberry___Leaf_scorch': {
                'name': 'Strawberry Leaf Scorch',
                'scientific_name': 'Diplocarpon earliana',
                'description': 'Leaf scorch is a fungal disease causing purple to brown spots on strawberry leaves, reducing plant vigor.',
                'symptoms': 'Small purple spots on leaves that expand; yellowing; leaf death; reduced fruit yield.',
                'cause': 'Fungal infection that overwinters in infected plant debris.',
                'treatment_organic': 'Remove infected leaves; apply sulfur; improve air circulation.',
                'treatment_chemical': 'Apply fungicides such as captan, myclobutanil, or azoxystrobin.',
                'prevention': 'Plant resistant varieties; space plants properly; remove infected debris.',
                'difficulty': 'Moderate'
            },
            'Strawberry___healthy': {
                'name': 'Healthy Strawberry',
                'scientific_name': 'Fragaria × ananassa',
                'description': 'Healthy strawberry plant with no visible disease symptoms. Strawberries require well-draining soil and mulching.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper mulching and renovation.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Proper spacing; adequate irrigation; regular renovation.',
                'difficulty': 'N/A'
            },
            
            # Tomato diseases
            'Tomato___Bacterial_spot': {
                'name': 'Tomato Bacterial Spot',
                'scientific_name': 'Xanthomonas vesicatoria',
                'description': 'Bacterial spot causes water-soaked lesions on tomato leaves, stems, and fruit, reducing yield and quality.',
                'symptoms': 'Small, water-soaked spots on leaves; yellow halos; raised scabby lesions on fruit.',
                'cause': 'Bacterial infection spread by water splash and contaminated tools.',
                'treatment_organic': 'Apply copper sprays; remove infected tissue; use disease-free seeds.',
                'treatment_chemical': 'Apply copper-containing bactericides or streptomycin (where registered).',
                'prevention': 'Use disease-free seeds; crop rotation; avoid overhead irrigation.',
                'difficulty': 'Moderate to High'
            },
            'Tomato___Early_blight': {
                'name': 'Tomato Early Blight',
                'scientific_name': 'Alternaria solani',
                'description': 'Early blight is a fungal disease causing dark concentric lesions on tomato leaves, starting from lower leaves.',
                'symptoms': 'Dark brown lesions with concentric rings on leaves; yellowing; stem cankers; fruit lesions.',
                'cause': 'Fungal infection that overwinters in soil and plant debris.',
                'treatment_organic': 'Remove infected leaves; apply copper fungicides; maintain plant vigor.',
                'treatment_chemical': 'Apply fungicides such as chlorothalonil, mancozeb, or azoxystrobin.',
                'prevention': 'Crop rotation; stake plants; avoid overhead irrigation; proper spacing.',
                'difficulty': 'Moderate'
            },
            'Tomato___Late_blight': {
                'name': 'Tomato Late Blight',
                'scientific_name': 'Phytophthora infestans',
                'description': 'Late blight is a devastating disease that rapidly kills tomato plants; same pathogen as potato late blight.',
                'symptoms': 'Water-soaked lesions on leaves; white fungal growth; black, firm fruit rot; rapid plant death.',
                'cause': 'Fungal-like pathogen that spreads rapidly in cool, wet conditions.',
                'treatment_organic': 'Remove infected plants immediately; apply copper fungicides.',
                'treatment_chemical': 'Apply fungicides such as mancozeb, chlorothalonil, or metalaxyl preventively.',
                'prevention': 'Avoid planting near potatoes; eliminate volunteer plants; provide good air circulation.',
                'difficulty': 'Very High'
            },
            'Tomato___Leaf_Mold': {
                'name': 'Tomato Leaf Mold',
                'scientific_name': 'Passalora fulva',
                'description': 'Leaf mold is a fungal disease causing yellow patches on upper leaf surfaces and olive-green growth underneath.',
                'symptoms': 'Pale yellow patches on upper leaf surface; olive-green mold underneath; leaf drop.',
                'cause': 'Fungal infection favored by high humidity and poor air circulation.',
                'treatment_organic': 'Improve air circulation; reduce humidity; remove infected leaves.',
                'treatment_chemical': 'Apply fungicides such as chlorothalonil, mancozeb, or azoxystrobin.',
                'prevention': 'Provide good air circulation; control humidity; space plants properly.',
                'difficulty': 'Low to Moderate'
            },
            'Tomato___Septoria_leaf_spot': {
                'name': 'Tomato Septoria Leaf Spot',
                'scientific_name': 'Septoria lycopersici',
                'description': 'Septoria leaf spot causes small circular spots with dark borders on tomato leaves, starting from lower leaves.',
                'symptoms': 'Small circular spots with dark borders and gray centers on leaves; yellowing; severe defoliation.',
                'cause': 'Fungal infection that overwinters in plant debris and soil.',
                'treatment_organic': 'Remove infected leaves; apply copper fungicides; mulch to prevent splash.',
                'treatment_chemical': 'Apply fungicides such as chlorothalonil, mancozeb, or azoxystrobin.',
                'prevention': 'Crop rotation; stake plants; mulch; avoid overhead irrigation.',
                'difficulty': 'Moderate'
            },
            'Tomato___Spider_mites Two-spotted_spider_mite': {
                'name': 'Tomato Spider Mites',
                'scientific_name': 'Tetranychus urticae',
                'description': 'Two-spotted spider mites are tiny pests that cause stippling and webbing on tomato leaves, reducing plant vigor.',
                'symptoms': 'Stippled yellow leaves; fine webbing; leaf bronzing; reduced plant growth.',
                'cause': 'Spider mite infestation; favored by hot, dry conditions.',
                'treatment_organic': 'Spray with water to dislodge mites; apply neem oil or insecticidal soap; release predatory mites.',
                'treatment_chemical': 'Apply miticides such as abamectin or bifenthrin (follow label instructions).',
                'prevention': 'Maintain adequate humidity; avoid broad-spectrum insecticides that kill predators.',
                'difficulty': 'Moderate'
            },
            'Tomato___Target_Spot': {
                'name': 'Tomato Target Spot',
                'scientific_name': 'Corynespora cassiicola',
                'description': 'Target spot causes concentric ring lesions on tomato leaves, stems, and fruit, similar to early blight.',
                'symptoms': 'Concentric ring lesions on leaves; stem lesions; fruit lesions with cracking.',
                'cause': 'Fungal infection favored by warm, wet conditions.',
                'treatment_organic': 'Remove infected tissue; improve air circulation; apply copper fungicides.',
                'treatment_chemical': 'Apply fungicides such as chlorothalonil, mancozeb, or azoxystrobin.',
                'prevention': 'Crop rotation; stake plants; avoid overhead irrigation; proper spacing.',
                'difficulty': 'Moderate'
            },
            'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
                'name': 'Tomato Yellow Leaf Curl Virus',
                'scientific_name': 'Tomato yellow leaf curl virus (TYLCV)',
                'description': 'TYLCV is a devastating virus transmitted by whiteflies, causing severe stunting and yield loss in tomatoes.',
                'symptoms': 'Upward curling of leaves; yellowing; severe stunting; flower abortion; reduced fruit set.',
                'cause': 'Viral infection transmitted by silverleaf whitefly; no cure once infected.',
                'treatment_organic': 'Remove infected plants immediately; control whiteflies with reflective mulches; use insect netting.',
                'treatment_chemical': 'Apply insecticides to control whitefly vectors; use imidacloprid or other systemic insecticides.',
                'prevention': 'Use virus-free transplants; control whiteflies; install insect netting; use resistant varieties.',
                'difficulty': 'Very High'
            },
            'Tomato___Tomato_mosaic_virus': {
                'name': 'Tomato Mosaic Virus',
                'scientific_name': 'Tomato mosaic virus (ToMV)',
                'description': 'Tomato mosaic virus causes mottling, mosaic patterns, and leaf distortion in tomatoes, reducing yield.',
                'symptoms': 'Mottled light and dark green areas; leaf curling and distortion; stunting; reduced fruit yield.',
                'cause': 'Viral infection spread by contaminated tools, hands, and tobacco products.',
                'treatment_organic': 'Remove infected plants; sanitize tools; avoid tobacco use while working with plants.',
                'treatment_chemical': 'No chemical cure; control insect vectors that may spread the virus.',
                'prevention': 'Use virus-free seeds; sanitize tools; wash hands; avoid tobacco near plants.',
                'difficulty': 'High'
            },
            'Tomato___healthy': {
                'name': 'Healthy Tomato',
                'scientific_name': 'Solanum lycopersicum',
                'description': 'Healthy tomato plant with no visible disease symptoms. Tomatoes require consistent moisture and support.',
                'symptoms': 'No visible disease symptoms; green, healthy leaves; normal fruit development.',
                'cause': 'Good growing conditions and proper care.',
                'treatment_organic': 'Continue regular maintenance; proper staking and pruning.',
                'treatment_chemical': 'No chemical treatment needed for healthy plants.',
                'prevention': 'Proper spacing; adequate irrigation; regular monitoring and maintenance.',
                'difficulty': 'N/A'
            }
        }
    
    def get_disease_info(self, disease_class):
        """
        Get comprehensive information about a disease
        
        Args:
            disease_class: The disease class name (e.g., 'Tomato___Early_blight')
            
        Returns:
            Dictionary with disease information or None if not found
        """
        return self.diseases.get(disease_class)
    
    def get_all_diseases(self):
        """Return all disease information"""
        return self.diseases
    
    def get_plant_type(self, disease_class):
        """Extract plant type from disease class name"""
        if '___' in disease_class:
            return disease_class.split('___')[0].replace('_', ' ')
        return 'Unknown'
    
    def get_disease_name(self, disease_class):
        """Extract disease name from disease class name"""
        if '___' in disease_class:
            return disease_class.split('___')[1].replace('_', ' ')
        return disease_class


# Singleton instance for app-wide use
_db_instance = None


def get_disease_db():
    """Get or create singleton database instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = DiseaseDatabase()
    return _db_instance
