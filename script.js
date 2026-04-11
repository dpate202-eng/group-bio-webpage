/**
 * DAN Team Bio — script.js
 * Uses event delegation and data attributes instead of inline onclick handlers.
 * Bio toggle animates via CSS class (no inline style juggling).
 */

document.addEventListener("DOMContentLoaded", () => {

  // ── Navigation ──────────────────────────────────────────────
  const navButtons = document.querySelectorAll(".nav-btn");
  const sections   = document.querySelectorAll(".section");

  navButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.dataset.section;

      // Update active nav button
      navButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      // Swap visible section
      sections.forEach(sec => {
        sec.classList.toggle("active", sec.id === target);
      });
    });
  });

  // ── Bio Toggles ─────────────────────────────────────────────
  document.querySelectorAll(".toggle-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const bioId = btn.dataset.bio;
      const bio   = document.getElementById(bioId);
      if (!bio) return;

      const isOpen = bio.classList.toggle("visible");
      btn.textContent = isOpen ? "Hide Bio" : "Show Bio";
      btn.classList.toggle("open", isOpen);
    });
  });

});
