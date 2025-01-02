class OrbsAnimation {
    constructor(canvas) {
      this.canvas = canvas;
      this.ctx = canvas.getContext('2d');
      this.orbs = [];
      this.colors = ['#F3C855', '#55E7F3', '#55F3A2',]; // '#F999BF', '#F3A255', '#F3E855'
      this.numberOfOrbs = 15;
      
      // Setup
      this.resizeCanvas();
      this.initOrbs();
      
      // Event listeners
      window.addEventListener('resize', () => this.resizeCanvas());
      canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
      
      // Start animation
      this.animate();
    }
  
    resizeCanvas() {
      this.canvas.width = window.innerWidth;
      this.canvas.height = window.innerHeight;
    }
  
    initOrbs() {
      this.orbs = [];
      for (let i = 0; i < this.numberOfOrbs; i++) {
        this.orbs.push({
          x: Math.random() * this.canvas.width,
          y: Math.random() * this.canvas.height,
          radius: Math.random() * 300 + 20,
          color: this.colors[Math.floor(Math.random() * this.colors.length)],
          dx: (Math.random() - 0.5) * 0.5,
          dy: (Math.random() - 0.5) * 0.5,
          opacity: Math.random() * 0.5 + 0.2
        });
      }
    }
  
    drawOrb(orb) {
      const gradient = this.ctx.createRadialGradient(
        orb.x, orb.y, 0,
        orb.x, orb.y, orb.radius
      );
      
      gradient.addColorStop(0, `${orb.color}${Math.floor(orb.opacity * 255).toString(16).padStart(2, '0')}`);
      gradient.addColorStop(1, `${orb.color}00`);
      
      this.ctx.beginPath();
      this.ctx.fillStyle = gradient;
      this.ctx.arc(orb.x, orb.y, orb.radius, 0, Math.PI * 2);
      this.ctx.fill();
    }
  
    handleMouseMove(e) {
      const rect = this.canvas.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;
      
      this.orbs.forEach(orb => {
        const dx = mouseX - orb.x;
        const dy = mouseY - orb.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        
        if (distance < 200) {
          const angle = Math.atan2(dy, dx);
          orb.dx -= Math.cos(angle) * 0.02;
          orb.dy -= Math.sin(angle) * 0.02;
        }
      });
    }
  
    animate() {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      
      this.orbs.forEach(orb => {
        // Update position
        orb.x += orb.dx;
        orb.y += orb.dy;
        
        // Bounce off walls
        if (orb.x - orb.radius < 0 || orb.x + orb.radius > this.canvas.width) {
          orb.dx = -orb.dx;
        }
        if (orb.y - orb.radius < 0 || orb.y + orb.radius > this.canvas.height) {
          orb.dy = -orb.dy;
        }
        
        // Draw the orb
        this.drawOrb(orb);
      });
      
      requestAnimationFrame(() => this.animate());
    }
}