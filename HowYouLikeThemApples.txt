trees = 333 				                                            #hoeveel bomen zijn er in totaal? 
shadeTrees = 222 			                                            #hoeveel bomen staan er in de schaduw (afgerond naar boven)? 
sunnyTrees = trees - shadeTrees			                                #hoeveel in de zon? 

shadeOutputModifier = 80 	                                            #hoeveel procent productie geeft een schaduwboom?
sunnyTreesOutput = 146		                                            #hoeveel appels geeft 1 zonnige boom?
shadeTreeOutput = (sunnyTreesOutput / 100) * shadeOutputModifier 		#hoeveel appels geeft 1 schaduw boom? 

sunnyOutput = sunnyTrees * sunnyTreesOutput			                    #hoeveel appels geven alle zonnige bomen?
shadeOutput = shadeTrees * shadeTreeOutput	                            #hoeveel appels geven alle schaduw bomen?
totalOutput = shadeOutput * sunnyOutput		                            #hoeveel appels zijn er in totaal? 

owners = 4 					                                            #met hoeveel mensen verdelen we de appels? 
eatCount = 1 				                                            #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn? 
sellableOutput = 10489		                                            #hoeveel appels zijn er over en dus verkoopbaar? 
cut = 10489		                                                        #hoeveel appels mag ik verkopen? 

print(trees - sunnyTrees)				                                #hoeveel bomen in de zon. 
print(sunnyTreesOutput / 100 * shadeOutputModifier)			            #hoeveel appels in een schadow boom. 
print(sunnyTreesOutput * sunnyTrees)				                    #hoeveel appels vallen van de zonne bomen.
print(116*222)				                                            #hoeveel appels vallen van alles bomen in de schaduw.
print(sunnyOutput + shadeOutput)			                            #hoeveel appels zijn er in totaal.

print(totalOutput / owners)			                                    #hoeveel appels per persoon kan je verdelen. 
print(cut)				                                            	#hoeveel appels mag ik verkopen.  
