let scene, camera, renderer, model;

        init();
        animate();

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, 700 / 600, 0.1, 1000);
            renderer = new THREE.WebGLRenderer({ alpha: true });
            renderer.setSize(700, 600);
            document.getElementById('main__image').appendChild(renderer.domElement);
            console.log("ADDED");
            const ambientLight = new THREE.AmbientLight(0xffffff, 4);
            scene.add(ambientLight);

            plight = new THREE.PointLight(0xffffff, 3);
            plight.position.copy(camera.position);
            scene.add(plight);
            

            const helper = new THREE.PointLightHelper(plight);
            //scene.add(helper);

            const loader = new THREE.GLTFLoader();
            loader.load('fsgn_pls.gltf', function (gltf) {
                model = gltf.scene;

                // Установка прозрачного материала для всех объектов в модели
                model.traverse(function (node) {
                    if (node.isMesh) {
                        node.material.transparent = true;
                    }
                });

                scene.add(model);
                model.rotation.y += 0.65; 

                // Начало анимации прыжка
                jumpAnimation();
            });
            camera.position.z = 0.675;

            // Добавление возможности вращать модель с помощью мыши
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableZoom = false;
            controls.minPolarAngle = Math.PI / 2;
            controls.maxPolarAngle = Math.PI / 2;
            controls.update();

            // Добавление реакции на изменение размера окна
            window.addEventListener('resize', onWindowResize);
        }

        function animate() {
            requestAnimationFrame(animate);
            if (model) {
                model.rotation.y += 0.0075; // Изменение угла вращения
            }
            renderer.render(scene, camera);
            plight.position.copy(camera.position);

        }

        // Функция для обновления камеры при изменении размера окна
        function onWindowResize() {
            const container = document.getElementById('main__image');
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        }

        // Функция для анимации прыжка
        function jumpAnimation() {
            const initialY = model.position.y;
            const targetY = initialY + 0.25;
            let direction = 1;

            function jump() {
                model.position.y += direction*((targetY - model.position.y) / 100 + 0.00025);
                if (model.position.y >= targetY) {
                    direction = -1;
                } else if (model.position.y <= initialY) {
                    direction = 1;
                }
            }

            function jumpLoop() {
                jump();
                renderer.render(scene, camera);
                requestAnimationFrame(jumpLoop);
            }

            //jumpLoop();
        }