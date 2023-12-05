
import re

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

def parseInput(lines):
        mapName = ""

        # dirty dirty parsing.. but it works?
        for line in lines[1:]:
            if line.startswith("seed"):
                mapName = "seedToSoil"
            elif line.startswith("soil"):
                mapName = "soilToFertilizer"
            elif line.startswith("fertilizer"):
                mapName = "fertilizerToWater"
            elif line.startswith("water"):
                mapName = "waterToLight"
            elif line.startswith("light"):
                mapName = "lightToTemperature"
            elif line.startswith("temperature"):
                mapName = "temperatureToHumidity"
            elif line.startswith("humidity"):
                mapName = "humidityToLocation"
            else:
                vals = re.findall(r"\d+", line)
                if len(vals) == 0:
                    continue
                if mapName == "seedToSoil":
                    seedToSoil.append(vals)
                elif mapName == "soilToFertilizer":
                    soilToFertilizer.append(vals)
                elif mapName == "fertilizerToWater":
                    fertilizerToWater.append(vals)
                elif mapName == "waterToLight":
                    waterToLight.append(vals)
                elif mapName == "lightToTemperature":
                    lightToTemperature.append(vals)
                elif mapName == "temperatureToHumidity":
                    temperatureToHumidity.append(vals)
                elif mapName == "humidityToLocation":
                    humidityToLocation.append(vals)

def mapSourceToDestination(unit, map):
    for m in map:
        sourceRangeStart = int(m[1])
        sourceRangeEnd = sourceRangeStart + int(m[2])
        if int(unit) in range(sourceRangeStart, sourceRangeEnd):
            x = int(unit) - sourceRangeStart
            y = int(m[0]) + x
            return y
    
    return unit

def mapDestinationToSource(unit, map):
    for m in map:
        destinationRangeStart = int(m[0])
        destinationRangeEnd = destinationRangeStart + int(m[2])
        if int(unit) in range(destinationRangeStart, destinationRangeEnd):
            x = int(unit) - destinationRangeStart
            y = int(m[1]) + x
            return y


def main():

    file_path = "../input.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()
    
        # Get the seeds
        seeds = re.findall(r"\d+ \d+", lines[0])

        results = []

        parseInput(lines)

        for seed in seeds:
            seedStart = int(seed.split()[0])
            seedRange = int(seed.split()[1])
            
            print(f"Seed: {seedStart} -> {seedStart + seedRange}")
            
            for i in range(seedRange):
                seed = seedStart + i
                soil = mapSourceToDestination(seed, seedToSoil)
                fertilizer = mapSourceToDestination(soil, soilToFertilizer)
                water = mapSourceToDestination(fertilizer, fertilizerToWater)
                light = mapSourceToDestination(water, waterToLight)
                temperature = mapSourceToDestination(light, lightToTemperature)
                humidity = mapSourceToDestination(temperature, temperatureToHumidity)
                location = mapSourceToDestination(humidity, humidityToLocation)

                print(seed, location)

                results.append(location)
        
        print(min(results))

if __name__ == "__main__":
    main()