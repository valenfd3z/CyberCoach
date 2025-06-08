import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos
database_url = os.getenv('DATABASE_URL', 'postgresql://cybercoach_db_lib6_user:DPcnVLgMbHGbKRjFYw4wpB02mBCnvC7y@dpg-d1129uemcj7s739pct7g-a.oregon-postgres.render.com/cybercoach_db_lib6')

# Crear el motor de la base de datos
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Ejecutar los inserts
    session.execute("""
    -- Insertar ejercicios de pecho
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Press de banca (barra)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-barbell-bench-press-front.mp4#t=0.1', 'pecho'),
    ('Press de banca (mancuernas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-dumbbell-bench-press-front_y8zKZJl.mp4#t=0.1', 'pecho'),
    ('Press inclinado (multipower)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Smithmachine-incline-bench-press-side.mp4#t=0.1', 'pecho'),
    ('Press inclinado (mancuernas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-dumbbell-incline-bench-press-front_q2q0T12.mp4#t=0.1', 'pecho'),
    ('Press de pecho (máquina)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-chest-press-side.mp4#t=0.1', 'pecho'),
    ('Aperturas (máquina)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-pec-fly-side.mp4#t=0.1', 'pecho'),
    ('Crossover (cables)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-cable-pec-fly-front.mp4#t=0.1', 'pecho'),
    ('Flexiones de brazos', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Bodyweight-push-up-front.mp4#t=0.1', 'pecho'),
    ('Fondos en paralelas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-weighted-dip-side.mp4#t=0.1', 'pecho');

    -- Insertar ejercicios de espalda
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Jalón al pecho (prono)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-pulldown-front.mp4#t=0.1', 'espalda'),
    ('Jalón al pecho (neutro)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-neutral-pulldown-front.mp4#t=0.1', 'espalda'),
    ('Remo con mancuernas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-row-unilateral-side.mp4#t=0.1', 'espalda'),
    ('Remo en T (máquina)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-plate-loaded-t-bar-row-front.mp4#t=0.1', 'espalda'),
    ('Remo en T (barra olímpica)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-landmine-t-bar-rows-side.mp4#t=0.1', 'espalda'),
    ('Remo con barra', 'https://media.musclewiki.com/media/uploads/videos/branded/male-barbell-bent-over-row-front.mp4#t=0.1', 'espalda'),
    ('Remo Gironda (polea)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-seated-cable-row-front.mp4#t=0.1', 'espalda'),
    ('Pull Over (poleas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-pullover-side.mp4#t=0.1', 'espalda'),
    ('Encogimientos', 'https://media.musclewiki.com/media/uploads/videos/branded/male-dumbbell-seated-shrug-front.mp4#t=0.1', 'espalda');

    -- Insertar ejercicios de hombro
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Press militar (barra)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-overhead-press-side.mp4#t=0.1', 'hombro'),
    ('Press militar (mancuernas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-dumbbell-seated-overhead-press-front.mp4#t=0.1', 'hombro'),
    ('Elevaciones laterales (mancuernas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-lateral-raise-front.mp4#t=0.1', 'hombro'),
    ('Elevaciones laterales (poleas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-lateral-raise-side.mp4#t=0.1', 'hombro'),
    ('Elevaciones frontales (barra)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-front-raise-front.mp4#t=0.1', 'hombro'),
    ('Elevaciones frontales (mancuernas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-front-raise-side.mp4#t=0.1', 'hombro'),
    ('Face Pull (polea)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-face-pulls-front.mp4#t=0.1', 'hombro'),
    ('Peck Deck invertido', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-reverse-fly-side.mp4#t=0.1', 'hombro'),
    ('Press Arnold', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-seated-arnold-press-front.mp4#t=0.1', 'hombro');

    -- Insertar ejercicios de bíceps
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Curl con barra', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-curl-front.mp4#t=0.1', 'bíceps'),
    ('Curl martillo', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-hammer-curl-front.mp4#t=0.1', 'bíceps'),
    ('Curl bayesiano con poleas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-bilateral-bayesian-curl-side.mp4#t=0.1', 'bíceps'),
    ('Curl predicador', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-preacher-curl-side.mp4#t=0.1', 'bíceps'),
    ('Curl inclinado', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-bench-braced-reverse-incline-curl-front.mp4#t=0.1', 'bíceps');

    -- Insertar ejercicios de tríceps
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Rompecráneos', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-skullcrusher-front.mp4#t=0.1', 'tríceps'),
    ('Extensiones en poleas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-push-down-front.mp4#t=0.1', 'tríceps'),
    ('Extensiones trasnuca', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-overhead-tricep-extension-front.mp4#t=0.1', 'tríceps'),
    ('Flexión cruzada', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-cross-pushdown-front.mp4#t=0.1', 'tríceps'),
    ('Press francés', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Kettlebells-kettlebell-standing-tricep-extension-front.mp4#t=0.1', 'tríceps'),
    ('Press tríceps en polea baja', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-overhead-tricep-press-front.mp4#t=0.1', 'tríceps');

    -- Insertar ejercicios de antebrazo
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Curl inverso (poleas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-reverse-curl-front.mp4#t=0.1', 'antebrazo'),
    ('Curl inverso (barra)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-barbell-behind-the-back-wrist-curl-front.mp4#t=0.1', 'antebrazo'),
    ('Curl de muñeca (mancuernas)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-wrist-curl-side.mp4#t=0.1', 'antebrazo'),
    ('Curl de muñeca (barra)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-wrist-curl-front.mp4#t=0.1', 'antebrazo'),
    ('Curl con mancuernas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-reverse-curl-front.mp4#t=0.1', 'antebrazo'),
    ('Curl con barra', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-reverse-curl-front.mp4#t=0.1', 'antebrazo');

    -- Insertar ejercicios de piernas
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Sentadillas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-high-bar-squat-front.mp4#t=0.1', 'piernas'),
    ('Sentadilla Sumo', 'https://media.musclewiki.com/media/uploads/videos/branded/male-dumbbell-sumo-squat-front.mp4#t=0.1', 'piernas'),
    ('Sentadilla Búlgara', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-bulgarian-split-squat-front.mp4#t=0.1', 'piernas'),
    ('Prensa 45°', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-leg-press-front.mp4#t=0.1', 'piernas'),
    ('Prensa Nitro', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-horizontal-leg-press-side.mp4#t=0.1', 'piernas'),
    ('Extensiones de cuádriceps', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-plate-loaded-leg-extension-side.mp4#t=0.1', 'piernas'),
    ('Peso Muerto Rumano', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-romanian-deadlift-side.mp4#t=0.1', 'piernas'),
    ('Peso Muerto Convencional', 'https://media.musclewiki.com/media/uploads/videos/branded/male-barbell-stiff-leg-deadlift-front.mp4#t=0.1', 'piernas'),
    ('Curl Femoral', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-hamstring-curl-front.mp4#t=0.1', 'piernas'),
    ('Hip Thrust', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-hip-thrust-front.mp4#t=0.1', 'piernas'),
    ('Patada de glúteos (cable)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-glute-kickback-side.mp4#t=0.1', 'piernas'),
    ('Elevaciones de gemelos (sentado)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-seated-calf-raise-front.mp4#t=0.1', 'piernas'),
    ('Elevaciones de gemelos (parado)', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-standing-calf-raises-side.mp4#t=0.1', 'piernas'),
    ('Sentadilla hack', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-machine-hack-squat-side.mp4#t=0.1', 'piernas'),
    ('Sentadilla hack horizontal', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Machine-horizontal-hack-squat-front.mp4#t=0.1', 'piernas');

    -- Insertar ejercicios de core
    INSERT INTO ejercicio (nombre, video_url, musculo) VALUES
    ('Crunch abdominal', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-roll-outs-side.mp4#t=0.1', 'core'),
    ('Elevación de piernas', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Bodyweight-laying-leg-raises-front.mp4#t=0.1', 'core'),
    ('Plancha', 'https://media.musclewiki.com/media/uploads/videos/branded/male-plate-weighted-forearm-plank-side.mp4#t=0.1', 'core'),
    ('Giros rusos', 'https://media.musclewiki.com/media/uploads/videos/branded/male-plate-russian-twist-front.mp4#t=0.1', 'core'),
    ('Espinales en banco', 'https://media.musclewiki.com/media/uploads/videos/branded/male-machine-back-extensions-side.mp4#t=0.1', 'core'),
    ('Superman', 'https://media.musclewiki.com/media/uploads/videos/branded/male-Bodyweight-supermans-side.mp4#t=0.1', 'core');
    """)
    
    session.commit()
    print("¡Datos insertados exitosamente!")

except Exception as e:
    session.rollback()
    print(f"Error al insertar datos: {str(e)}")
    raise
finally:
    session.close()
