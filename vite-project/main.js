import * as THREE from 'three';

//Scene
const scene = new THREE.Scene();

//create sphere
const geometry = new THREE.SphereGeometry(3,64,64);//半徑,hor line ,ver line
const material = new THREE.MeshBasicMaterial( { color: "#00ff83" } ); 
const mesh = new THREE.Mesh( geometry, material );
scene.add(mesh);

//sizes
const sizes = {
  width: window.innerWidth,
  height:window.innerHeight,
}

//light
const light = new THREE.PointLight(0xffffff, 1, 100)
light.position.set(0, 10, 10);
scene.add(light);

//camera
const camera = new THREE.PerspectiveCamera( 75, sizes.width / sizes.height, 0.1, 100 );//45deg aspectRatio min max
camera.position.z = 20;
scene.add(camera);

//renderer
const canvas = document.querySelector('.webgl');
const renderer = new THREE.WebGL1Renderer({canvas});
renderer.setSize(sizes.width,sizes.height);
renderer.render(scene,camera);

window.addEventListener('resize',()=>{
  sizes.width=window.innerWidth;
  sizes.height=window.innerHeight;

  camera.aspect = sizes.width / sizes.height
  camera.updateProjectionMatrix();
  renderer.setSize(sizes.width, sizes.height);
})

const loop = () => {
  mesh.rotation.x += .1
  renderer.render(scene,camera);
  window.requestAnimationFrame(loop)
}
loop();