package vm_vs_docker_benchmark.scripts;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

// Interface estrategia
interface EstrategiaJuego {
    int aplicarEstrategia(int habilidadTotal);
}

// Estrategia Ataque Rápido
class AtaqueRapido implements EstrategiaJuego {
    public int aplicarEstrategia(int habilidadTotal) {
        return (int)(habilidadTotal * 1.1);
    }
}

// Estrategia Defensa Fuerte
class DefensaFuerte implements EstrategiaJuego {
    public int aplicarEstrategia(int habilidadTotal) {
        return (int)(habilidadTotal * 0.9 + 10);
    }
}

// Clase Jugador
class Jugador {
    private String nombre;
    private int habilidad; // 0-100

    public Jugador(String nombre, int habilidad) {
        this.nombre = nombre;
        this.habilidad = habilidad;
    }

    public int getHabilidad() {
        return habilidad;
    }

    public String getNombre() {
        return nombre;
    }
}

// Clase Equipo
class Equipo {
    private String nombre;
    private List<Jugador> jugadores;
    private EstrategiaJuego estrategia;

    public Equipo(String nombre, EstrategiaJuego estrategia) {
        this.nombre = nombre;
        this.estrategia = estrategia;
        this.jugadores = new ArrayList<>();
    }

    public void agregarJugador(Jugador j) {
        jugadores.add(j);
    }

    public int calcularFuerza() {
        int total = 0;
        for (Jugador j : jugadores) {
            total += j.getHabilidad();
        }
        return estrategia.aplicarEstrategia(total);
    }

    public String getNombre() {
        return nombre;
    }
}

// Clase Partido
class Partido {
    private Equipo equipo1, equipo2;

    public Partido(Equipo equipo1, Equipo equipo2) {
        this.equipo1 = equipo1;
        this.equipo2 = equipo2;
    }

    public void jugar() {
        int fuerza1 = equipo1.calcularFuerza();
        int fuerza2 = equipo2.calcularFuerza();

        Random rand = new Random();
        int goles1 = rand.nextInt(fuerza1 / 30 + 1);
        int goles2 = rand.nextInt(fuerza2 / 30 + 1);

        System.out.println("\nResultado del partido:");
        System.out.println(equipo1.getNombre() + " " + goles1 + " - " + goles2 + " " + equipo2.getNombre());

        if (goles1 > goles2) {
            System.out.println("¡Gana " + equipo1.getNombre() + "!");
        } else if (goles2 > goles1) {
            System.out.println("¡Gana " + equipo2.getNombre() + "!");
        } else {
            System.out.println("¡Empate!");
        }
    }
}

// Clase principal con nombre "Fifa"
public class Fifa {
    public static void main(String[] args) {
        Equipo barcelona = new Equipo("Barcelona", new AtaqueRapido());
        Equipo madrid = new Equipo("Real Madrid", new DefensaFuerte());

        barcelona.agregarJugador(new Jugador("Messi", 95));
        barcelona.agregarJugador(new Jugador("Xavi", 90));

        madrid.agregarJugador(new Jugador("Cristiano", 94));
        madrid.agregarJugador(new Jugador("Modric", 91));

        Partido partido = new Partido(barcelona, madrid);
        partido.jugar();
    }
}


