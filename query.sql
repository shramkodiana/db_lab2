SELECT species.dino_species AS species, COUNT(dinosaur.species_id) FROM dinosaur
JOIN species ON species.species_id = dinosaur.species_id
GROUP BY dino_species;

SELECT diet.dino_diet AS diet, COUNT(dinosaur.diet_id) FROM dinosaur 
JOIN diet ON diet.diet_id = dinosaur.diet_id
GROUP BY dino_diet;

SELECT dino_name, length_in_meters FROM dinosaur
ORDER BY length_in_meters DESC;