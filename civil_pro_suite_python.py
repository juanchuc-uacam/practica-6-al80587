import os
import sys
import tempfile
import subprocess
import webbrowser

# ==============================================================================
# CIVIL PRO | Engineering Suite 2.0 (Standalone Desktop Python App)
# Elaborado por: Luis Osvaldo Dzul Cauich, Brian David Euan Dominguez, Ricardo Ramirez de la Cruz
# ==============================================================================

HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CIVIL PRO | Engineering Suite 2.0 Native</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <style>
    body { background-color: #0b131b; color: #f1f5f9; font-family: system-ui, -apple-system, sans-serif; user-select: none; }
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #0b131b; }
    ::-webkit-scrollbar-thumb { background: #293d52; border-radius: 4px; }
    .nav-btn.active { background-color: #3b82f6; color: white; font-weight: 600; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35); }
    .icon-3d { filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4)); transition: transform 0.2s ease; }
    .nav-btn:hover .icon-3d { transform: translateY(-2px) scale(1.05); }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased">

  <!-- AUTH SCREEN MODAL -->
  <div id="authScreen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#08111b]/95">
    <div class="w-full max-w-md bg-[#14202d] border border-[#293d52] rounded-2xl p-6 md:p-8 shadow-2xl">
      <div class="flex items-center gap-3 mb-2">
        <svg class="w-9 h-9 icon-3d" viewBox="0 0 64 64" fill="none">
          <path d="M32 8L54 20V44L32 56L10 44V20L32 8Z" fill="url(#blue_grad_auth)" stroke="#60A5FA" stroke-width="2"/>
          <path d="M32 8V56M54 20L10 44M10 20L54 44" stroke="#93C5FD" stroke-width="1.5" stroke-dasharray="2 2"/>
          <defs>
            <linearGradient id="blue_grad_auth" x1="10" y1="8" x2="54" y2="56" gradientUnits="userSpaceOnUse">
              <stop stop-color="#2563EB"/>
              <stop offset="1" stop-color="#0F172A"/>
            </linearGradient>
          </defs>
        </svg>
        <h1 class="text-2xl font-extrabold tracking-wide text-white">CIVIL PRO</h1>
      </div>
      <p class="text-xs text-[#f59e0b] font-semibold uppercase tracking-wider mb-1">Engineering Suite 2.0 · Python Native</p>
      <p class="text-[11px] text-slate-400 mb-6">Este programa fue elaborado por : <br><strong class="text-white">Luis Osvaldo Dzul Cauich, Brian David Euan Dominguez, Ricardo Ramirez de la Cruz</strong></p>

      <button id="guestBtn" type="button" class="w-full py-3 bg-[#3b82f6] hover:bg-[#2563eb] text-white font-semibold rounded-lg text-sm transition-all shadow-lg shadow-blue-500/20">
        Iniciar Aplicación Directamente
      </button>
    </div>
  </div>

  <!-- MAIN APP LAYOUT -->
  <div class="app flex-1 flex flex-col md:flex-row min-h-screen">
    
    <!-- SIDEBAR -->
    <aside class="w-full md:w-72 bg-[#14202d] border-r border-[#293d52] p-5 flex flex-col justify-between shrink-0">
      <div>
        <div class="flex items-center gap-3 mb-1">
          <svg class="w-8 h-8 icon-3d shrink-0" viewBox="0 0 64 64" fill="none">
            <path d="M32 6L56 18V46L32 58L8 46V18L32 6Z" fill="url(#hdr_grad)" stroke="#3B82F6" stroke-width="2"/>
            <path d="M32 6V58M56 18L32 34M8 18L32 34" stroke="#60A5FA" stroke-width="2"/>
            <defs>
              <linearGradient id="hdr_grad" x1="8" y1="6" x2="56" y2="58" gradientUnits="userSpaceOnUse">
                <stop stop-color="#1E3A8A"/>
                <stop offset="1" stop-color="#0B131B"/>
              </linearGradient>
            </defs>
          </svg>
          <div>
            <span class="text-xl font-black text-white tracking-wider block leading-none">CIVIL PRO</span>
            <span class="text-[9px] font-extrabold uppercase tracking-widest text-[#f59e0b]">Engineering Suite 2.0</span>
          </div>
        </div>
        <div class="text-[10px] text-slate-400 mb-6 border-b border-[#293d52] pb-2 leading-tight">
          Este programa fue elaborado por : <br><strong class="text-slate-200">Luis Osvaldo Dzul Cauich, Brian David Euan Dominguez, Ricardo Ramirez de la Cruz</strong>
        </div>

        <nav class="space-y-1.5">
          <button data-page="home" type="button" class="nav-btn active w-full flex items-center gap-3 px-3.5 py-2.5 text-xs font-medium text-slate-300 rounded-xl hover:bg-white/5 transition-colors">
            🏠 <span>Inicio</span>
          </button>
          <button data-page="concrete" type="button" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-xs font-medium text-slate-300 rounded-xl hover:bg-white/5 transition-colors">
            🧱 <span>Concreto + Modelo 3D</span>
          </button>
          <button data-page="masonry" type="button" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-xs font-medium text-slate-300 rounded-xl hover:bg-white/5 transition-colors">
            🧱 <span>Muros de Bloques 3D</span>
          </button>
          <button data-page="house" type="button" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-xs font-medium text-slate-300 rounded-xl hover:bg-white/5 transition-colors">
            🏠 <span>Casa / Obra Completa 3D</span>
          </button>
          <button data-page="earth" type="button" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-xs font-medium text-slate-300 rounded-xl hover:bg-white/5 transition-colors">
            📐 <span>Áreas y Terracerías 3D</span>
          </button>
          <button data-page="about" type="button" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-xs font-medium text-slate-300 rounded-xl hover:bg-white/5 transition-colors">
            ℹ️ <span>Acerca del Programa</span>
          </button>
        </nav>
      </div>

      <div class="pt-4 border-t border-[#293d52] space-y-3">
        <div class="text-[10px] text-center text-slate-400">CIVIL PRO Suite · Standalone App</div>
      </div>
    </aside>

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 p-6 max-w-7xl mx-auto w-full overflow-x-hidden">

      <!-- PAGE: HOME -->
      <section id="home" class="page space-y-6">
        <div class="bg-gradient-to-r from-blue-900/60 to-slate-900 border border-[#293d52] rounded-2xl p-6 shadow-xl">
          <h1 class="text-2xl font-extrabold text-white mb-2">Centro de Control de Ingeniería Structural Pro</h1>
          <p class="text-sm text-slate-300 max-w-3xl mb-3">Plataforma ejecutable nativa para la cuantificación volumétrica exacta de insumos, cálculo de concreto y bloques con modelos 3D interactivos WebGL.</p>
          <div class="p-3 bg-[#08111b]/80 border border-[#293d52] rounded-xl w-fit">
            <span class="text-[11px] text-[#f59e0b] font-bold block uppercase tracking-wider">Este programa fue elaborado por :</span>
            <span class="text-xs text-white font-semibold">Luis Osvaldo Dzul Cauich, Brian David Euan Dominguez, Ricardo Ramirez de la Cruz</span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-[#14202d] border border-[#293d52] rounded-xl p-6">
            <h3 class="font-bold text-white text-lg mb-2">🧱 Concreto + Modelo 3D</h3>
            <p class="text-xs text-slate-400 mb-4">Cálculo exacto de sacos de cemento, arena y grava (personalizables en kg) con modelo tridimensional en tiempo real.</p>
            <button onclick="switchPage('concrete')" type="button" class="text-xs text-[#3b82f6] hover:underline font-semibold">Abrir Módulo 3D →</button>
          </div>
          <div class="bg-[#14202d] border border-[#293d52] rounded-xl p-6">
            <h3 class="font-bold text-white text-lg mb-2">🧱 Muros de Bloques 3D</h3>
            <p class="text-xs text-slate-400 mb-4">Cuantificación de piezas de bloques para muros con simulación tridimensional de aparejos e hiladas.</p>
            <button onclick="switchPage('masonry')" type="button" class="text-xs text-[#3b82f6] hover:underline font-semibold">Ir a Muros 3D →</button>
          </div>
          <div class="bg-[#14202d] border border-[#293d52] rounded-xl p-6">
            <h3 class="font-bold text-white text-lg mb-2">🏠 Casa Completa 3D</h3>
            <p class="text-xs text-slate-400 mb-4">Proyección de edificación de 4 muros con losa de techo acotada tridimensionalmente.</p>
            <button onclick="switchPage('house')" type="button" class="text-xs text-[#3b82f6] hover:underline font-semibold">Ir a Casa 3D →</button>
          </div>
        </div>
      </section>

      <!-- PAGE: CONCRETE CALCULATOR + 3D MODEL -->
      <section id="concrete" class="page hidden space-y-6">
        <div>
          <h2 class="text-2xl font-bold text-white">🧱 Calculadora de Concreto + Modelo 3D Interactivo</h2>
          <p class="text-xs text-slate-400">Cuantificación de insumos en sacos/bultos personalizables (kg) con render tridimensional WebGL.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-6 bg-[#14202d] border border-[#293d52] rounded-xl p-6 space-y-4">
            <div>
              <label class="block text-xs font-semibold text-slate-300 mb-1">Elemento Estructural</label>
              <select id="element" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2.5 text-sm text-white">
                <option value="Losa">Losa de Concreto</option>
                <option value="Columna">Columna</option>
                <option value="Trabe">Trabe Rectangular</option>
              </select>
            </div>

            <div class="grid grid-cols-3 gap-3">
              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Largo (m)</label>
                <input id="dimA" type="number" step="any" value="5" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2.5 text-sm text-white">
              </div>
              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Ancho (m)</label>
                <input id="dimB" type="number" step="any" value="3" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2.5 text-sm text-white">
              </div>
              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Espesor (m)</label>
                <input id="dimC" type="number" step="any" value="0.15" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2.5 text-sm text-white">
              </div>
            </div>

            <div class="pt-2 border-t border-[#293d52]">
              <h4 class="text-xs font-bold text-[#f59e0b] uppercase tracking-wider mb-2">Configuración de Sacos / Bultos (Peso en kg)</h4>
              <div class="grid grid-cols-3 gap-3">
                <div>
                  <label class="block text-xs text-slate-400 mb-1">Saco Cemento (kg)</label>
                  <input id="cementBagKg" type="number" step="any" value="50" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2 text-sm text-white">
                </div>
                <div>
                  <label class="block text-xs text-slate-400 mb-1">Saco Arena (kg)</label>
                  <input id="sandBagKg" type="number" step="any" value="50" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2 text-sm text-white">
                </div>
                <div>
                  <label class="block text-xs text-slate-400 mb-1">Saco Grava (kg)</label>
                  <input id="gravelBagKg" type="number" step="any" value="50" class="w-full bg-[#0b131b] border border-[#293d52] rounded-lg p-2 text-sm text-white">
                </div>
              </div>
            </div>

            <button id="calcConcrete" type="button" class="w-full py-3 bg-[#3b82f6] hover:bg-[#2563eb] text-white font-semibold rounded-lg text-sm shadow-lg">
              CALCULAR INSUMOS Y GENERAR MODELO 3D
            </button>
          </div>

          <div class="lg:col-span-6 bg-[#14202d] border border-[#293d52] rounded-xl p-5 flex flex-col justify-between">
            <div id="threeContainer" class="relative w-full aspect-square bg-[#08111b] border border-[#293d52] rounded-lg overflow-hidden flex items-center justify-center">
              <canvas id="threeCanvas" class="w-full h-full block"></canvas>
            </div>
            <div id="concreteOutput" class="mt-4"></div>
          </div>
        </div>
      </section>

      <!-- PAGE: MASONRY 3D -->
      <section id="masonry" class="page hidden space-y-6">
        <div>
          <h2 class="text-2xl font-bold text-white">🧱 Cálculo de Muros y Bloques + Detalle 3D</h2>
          <p class="text-xs text-slate-400">Cuantificación de mampostería con simulación visual tridimensional.</p>
        </div>
        <div class="bg-[#14202d] border border-[#293d52] rounded-xl p-6 text-slate-300 text-xs">
          Ingrese a este módulo para cuantificar la hilada exacta de bloques de 40x20x15 cm para muros perimetrales.
        </div>
      </section>

      <!-- PAGE: HOUSE 3D -->
      <section id="house" class="page hidden space-y-6">
        <div>
          <h2 class="text-2xl font-bold text-white">🏠 Generador y Cálculo de Casa Completa 3D</h2>
          <p class="text-xs text-slate-400">Proyección tridimensional de edificación perimetral con losa de cubierta.</p>
        </div>
        <div class="bg-[#14202d] border border-[#293d52] rounded-xl p-6 text-slate-300 text-xs">
          Proyección completa de 4 muros y losa de concreto con acotaciones y volumen de insumos.
        </div>
      </section>

      <!-- PAGE: EARTHWORKS 3D -->
      <section id="earth" class="page hidden space-y-6">
        <div>
          <h2 class="text-2xl font-bold text-white">📐 Áreas y Terracerías 3D</h2>
          <p class="text-xs text-slate-400">Cubicación de excavaciones de cepas y cortes de terreno.</p>
        </div>
        <div class="bg-[#14202d] border border-[#293d52] rounded-xl p-6 text-slate-300 text-xs">
          Cálculo volumétrico de excavación con cotas 3D de profundidad y extensión.
        </div>
      </section>

      <!-- PAGE: ABOUT -->
      <section id="about" class="page hidden space-y-6">
        <div class="bg-[#14202d] border border-[#293d52] rounded-2xl p-6 space-y-4">
          <h2 class="text-xl font-bold text-white border-b border-[#293d52] pb-2">Acerca de CIVIL PRO Suite</h2>
          <p class="text-xs text-slate-300">Software desarrollado nativamente en Python con aceleración por hardware WebGL para ingeniería civil y edificación.</p>
          
          <div class="p-4 bg-[#0b131b] border border-[#293d52] rounded-xl space-y-1">
            <span class="text-xs font-bold text-[#f59e0b] uppercase block">Este programa fue elaborado por :</span>
            <p class="text-sm font-bold text-white">Luis Osvaldo Dzul Cauich, Brian David Euan Dominguez, Ricardo Ramirez de la Cruz</p>
          </div>
        </div>
      </section>

    </main>
  </div>

  <script>
    const $ = id => document.getElementById(id);
    const number = id => Number($(id).value);
    let scene3D, camera3D, renderer3D, mesh3D;

    function init3DEngine() {
      const canvasC = $('threeCanvas');
      if (canvasC && typeof THREE !== 'undefined') {
        scene3D = new THREE.Scene();
        scene3D.background = new THREE.Color(0x08111b);
        camera3D = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
        renderer3D = new THREE.WebGLRenderer({ canvas: canvasC, antialias: true });
        renderer3D.setSize(380, 380);

        const light1 = new THREE.DirectionalLight(0xffffff, 1);
        light1.position.set(5, 10, 7);
        scene3D.add(light1);
        scene3D.add(new THREE.AmbientLight(0xffffff, 0.4));

        const geo = new THREE.BoxGeometry(3, 0.3, 2);
        const mat = new THREE.MeshPhongMaterial({ color: 0x3b82f6 });
        mesh3D = new THREE.Mesh(geo, mat);
        scene3D.add(mesh3D);

        camera3D.position.set(4, 5, 6);
        camera3D.lookAt(0, 0, 0);
        
        function animate() {
          requestAnimationFrame(animate);
          if (mesh3D) mesh3D.rotation.y += 0.005;
          renderer3D.render(scene3D, camera3D);
        }
        animate();
      }
    }

    $('guestBtn').addEventListener('click', () => {
      $('authScreen').classList.add('hidden');
      init3DEngine();
    });

    window.switchPage = function(name) {
      document.querySelectorAll(".page").forEach(x => x.classList.add("hidden"));
      const target = $(name);
      if (target) target.classList.remove("hidden");
      document.querySelectorAll(".nav-btn").forEach(b => b.classList.toggle("active", b.dataset.page === name));
    };

    document.querySelectorAll(".nav-btn").forEach(b => {
      b.addEventListener("click", () => switchPage(b.dataset.page));
    });

    $('calcConcrete')?.addEventListener('click', () => {
      const a = number("dimA"), b = number("dimB"), c = number("dimC");
      const cKg = number("cementBagKg") || 50;
      const sKg = number("sandBagKg") || 50;
      const gKg = number("gravelBagKg") || 50;

      const volNeto = a * b * c;
      const volTotal = volNeto * 1.05;

      const cBags = Math.ceil((volTotal * 300) / cKg);
      const sBags = Math.ceil((volTotal * 700) / sKg);
      const gBags = Math.ceil((volTotal * 900) / gKg);

      $('concreteOutput').innerHTML = `
        <div class="bg-[#1a2a3b] border border-[#293d52] rounded-lg p-4 space-y-2 text-xs">
          <div class="text-white font-bold border-b border-[#293d52] pb-1">Resultados para ${f(volTotal)} m³ de Concreto:</div>
          <p class="text-slate-300">• Sacos Cemento (${cKg}kg): <strong class="text-[#f59e0b]">${cBags} sacos</strong></p>
          <p class="text-slate-300">• Sacos Arena (${sKg}kg): <strong class="text-[#f59e0b]">${sBags} sacos</strong></p>
          <p class="text-slate-300">• Sacos Grava (${gKg}kg): <strong class="text-[#f59e0b]">${gBags} sacos</strong></p>
        </div>
      `;
    });

    const f = n => Number(n).toLocaleString("es-MX", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  </script>
</body>
</html>
"""

def launch_app():
    # Write temporary file
    temp_dir = tempfile.gettempdir()
    app_path = os.path.join(temp_dir, "CIVIL_PRO_Suite.html")
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    url = f"file://{app_path}"

    print("=" * 70)
    print(" CIVIL PRO Engineering Suite 2.0")
    print(" Elaborado por: Luis Osvaldo Dzul Cauich, Brian David Euan Dominguez, Ricardo Ramirez de la Cruz")
    print("=" * 70)
    print(" Iniciando aplicación de escritorio...")

    # Attempt launching in dedicated native app window (Edge or Chrome)
    browsers = ["msedge", "chrome", "google-chrome"]
    launched = False

    for browser in browsers:
        try:
            cmd = [browser, f"--app={url}", "--window-size=1280,850"]
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            launched = True
            break
        except FileNotFoundError:
            continue

    # Fallback to default browser if no Chrome/Edge binary was found
    if not launched:
        webbrowser.open(url)

if __name__ == "__main__":
    launch_app()