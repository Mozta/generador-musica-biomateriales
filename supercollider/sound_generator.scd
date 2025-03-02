// Iniciar el servidor
s.boot;

// Ruta donde se guardará la grabación
~filePath = "~/SuperCollider/recordings/majo_sound.wav".standardizePath;

// Asegurar que el servidor está listo para grabar
s.prepareForRecord;

// Cuencos tibetanos (mejorado)
SynthDef(\tibetan_bowl, {
    |freq = 200, gain = -12|
    var strike, bowl, env, sig, reverb, resonances;

    strike = LPF.ar(WhiteNoise.ar(0.1), freq * 2) * EnvGen.kr(Env.perc(0.005, 0.3), doneAction: 0);

    resonances = Mix.ar([
        CombN.ar(strike, 0.2, 1 / freq, 2),
        CombN.ar(strike, 0.2, 1 / (freq * 1.5), 3),
        CombN.ar(strike, 0.2, 1 / (freq * 2.1), 4)
    ]);

    bowl = Mix.ar(SinOsc.ar([freq, freq * 1.5, freq * 2.1], 0, 0.15));
    env = EnvGen.kr(Env.perc(0.5, 6), doneAction: 2);
    reverb = GVerb.ar((bowl + resonances) * env, 15, 2.5, damping: 0.7, inputbw: 0.9, drylevel: 0.5, earlyreflevel: 0.3, taillevel: 0.4);

    Out.ar(0, reverb * gain.dbamp ! 2);
}).add;

// Piano etéreo (mejorado)
SynthDef(\ethereal_piano, {
    |freq = 440, amp = 0.7, reverb_amt = 0.7|
    var sig, env, chord, reverb;

    chord = [0, 3, 7].midicps + freq;
    sig = Mix.new(SinOsc.ar(chord, 0, amp * 0.5));
    env = EnvGen.kr(Env.perc(0.1, 4), doneAction: 2);
    sig = sig * env;
    reverb = FreeVerb.ar(sig, reverb_amt, 0.9, 0.7);

    Out.ar(0, reverb);
}).add;

// Ambient Synth
SynthDef(\ambient_synth, {
    |freq = 136, amp = 0.4|
    var sig, env, filtered, chorus, reverb;

    sig = LFSaw.ar(freq * [1, 1.01], 0, 0.2) + SinOsc.ar(freq * [1.5, 1.52], 0, 0.2);

    env = EnvGen.kr(Env.perc(1.5, 8), doneAction: 2);
    sig = sig * env;

    filtered = LPF.ar(sig, 1200);

    chorus = Mix.new([filtered, DelayC.ar(filtered, 0.1, LFNoise1.kr(0.1).range(0.01, 0.05))]);

    reverb = FreeVerb.ar(chorus, 0.9, 0.8, 0.5);

    Out.ar(0, reverb);
}).add;

// Recepción de OSC optimizada
(
OSCdef(\sensor1_control, { |msg|
    var freq = msg[1].clip(120, 400);
    Synth(\tibetan_bowl, [\freq, freq, \gain, -15]);
}, "/sensor1");

OSCdef(\sensor2_control, { |msg|
    var freq = msg[1].clip(200, 700), reverb_amt = msg[2].clip(0.3, 0.9);
    Synth(\ethereal_piano, [\freq, freq, \reverb_amt, reverb_amt]);
}, "/sensor2");

OSCdef(\sensor3_control, {
    |msg|
    var freq = msg[1].clip(136, 500);
    Synth(\ambient_synth, [\freq, freq]);
}, "/sensor3");

// Sensores adicionales: Temperatura y Luz
OSCdef(\sensor_temp, { |msg|
    var mod_factor = msg[1].clip(0.8, 1.2);
    Synth(\ambient_synth, [\mod_factor, mod_factor]);
}, "/sensor_temp");

OSCdef(\sensor_light, { |msg|
    var reverb_amt = msg[1].clip(0.3, 0.9);
    Synth(\ethereal_piano, [\reverb_amt, reverb_amt]);
}, "/sensor_light");
)

// Receptor para iniciar la grabación con una ruta específica
OSCdef(\startRecording, { |msg|
    s.record(path: ~filePath, numChannels: 2, headerFormat: "wav", sampleFormat: "int16");
    ("Grabación iniciada en: " + ~filePath).postln;
}, '/startRecording');

// Receptor para detener la grabación
OSCdef(\stopRecording, { |msg|
    s.stopRecording;
    ("Grabación detenida. Archivo guardado en: " + ~filePath).postln;
}, '/stopRecording');
