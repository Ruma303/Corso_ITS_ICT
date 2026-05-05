trait Drive { fn drive(&self); }
trait Fly { fn fly(&self); }
trait LandOnTheMoon { fn land_on_the_moon(&self); }

// Supertraits
trait FlyingCar: Drive + Fly {}
trait MoonCar: Drive + Fly + LandOnTheMoon {}

struct Engine { hp: i32 }
struct Wing { number: i32 }
struct Wheel { number: i32, diameter: i32 }

// Composed structs
struct Car { engine: Engine, wheels: Wheel }
struct Drone { engine: Engine, wings: Wing }
struct AdvancedVehicle {
    engine: Engine,
    wheels: Wheel,
    wings: Wing
}

// Blocchi impl generici per struct
impl Car {
    fn new(engine_hp: i32, wheel_count: i32, wheel_diameter: i32) -> Self {
        Self {
         engine: Engine { hp: engine_hp },
         wheels: Wheel { number: wheel_count, diameter: wheel_diameter }
        }
    }
}

impl Drone {
    fn new(engine_hp: i32, wings_number: i32) -> Self {
        Self {
            engine: Engine { hp: engine_hp },
            wings: Wing { number: wings_number }
        }
    }
}

impl AdvancedVehicle {
    fn new(engine_hp: i32, wheel_number: i32, wheel_diameter: i32, wing_number: i32) -> Self {
        Self {
            engine: Engine { hp: engine_hp },
            wheels: Wheel { number: wheel_number, diameter: wheel_diameter },
            wings: Wing { number: wing_number }
        }
    }
}

// Specifici traits per struct
impl Drive for Car {
    fn drive(&self) {
        println!("The car has {}hp", self.engine.hp)
    }
}

impl Drive for Drone {
    fn drive(&self) { println!("The drone can drive"); }
}

impl Fly for Drone {
    fn fly(&self) { println!("The drone is flying"); }
}

// 1. Implementa i trait base
impl Drive for AdvancedVehicle {
    fn drive(&self) { println!("Guido..."); }
}

impl Fly for AdvancedVehicle {
    fn fly(&self) { println!("Volo..."); }
}

impl LandOnTheMoon for AdvancedVehicle {
    fn land_on_the_moon(&self) {
        println!("The advanced vehicle is landing on the moon")
    }
}

// 2. Implementa il trait "unione" (vuoto, serve solo come firma)

// --- IMPLEMENT THE ALIASES ---
// Questi blocchi sono vuoti perché servono solo a dire al compilatore:
// "Sì, questo oggetto soddisfa i requisiti di FlyingCar/MoonCar"
impl FlyingCar for AdvancedVehicle {}
impl MoonCar for AdvancedVehicle {}

fn main() {
    println!("Hello, world!");
}
