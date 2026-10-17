import { defineMermaidSetup } from '@slidev/types'

// Deck-wide Mermaid config (Academic Teal palette, mirrors styles/index.css).
// htmlLabels:false keeps labels as pure SVG <text> so no foreignObject is
// emitted and the output stays self-contained.
export default defineMermaidSetup(() => {
  return {
    theme: 'base',
    themeVariables: {
      fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif",
      fontSize: '14px',
      primaryColor: '#F8FAFC',
      primaryBorderColor: '#CED5D7',
      primaryTextColor: '#172327',
      lineColor: '#64748B',
      edgeLabelBackground: '#FFFFFF',
    },
    flowchart: {
      htmlLabels: false,
      nodeSpacing: 28,
      rankSpacing: 42,
      curve: 'linear',
      padding: 8,
    },
  }
})
