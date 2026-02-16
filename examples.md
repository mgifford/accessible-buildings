---
layout: page
title: Examples
permalink: /examples/
---

# Examples and Benchmarks

The best way to learn how to build a great access guide is to see how others have done it. We've collected examples of building access guides and evaluated them against our [Toolkit Rubric](#the-evaluation-rubric).

## Example Guides

<div class="example-grid">
  {% for example in site.examples %}
    <div class="example-card">
      <h3><a href="{{ example.url }}">{{ example.title }}</a></h3>
      <p><strong>Type:</strong> {{ example.building_type }} ({{ example.country }})</p>
      <p><strong>Last Reviewed:</strong> {{ example.last_reviewed }}</p>
      <a href="{{ example.url }}" class="button">View Evaluation</a>
    </div>
  {% endfor %}
</div>

---

## The Evaluation Rubric

Every example in this collection is assessed against eight criteria:

1. **Discoverability:** Is it easy to find from the footer, contact, and visit pages?
2. **Arrival Clarity:** Does it cover transit, taxi, cycling, and driving?
3. **Entrance Clarity:** Are step-free routes and door types clearly described?
4. **Internal Navigation:** Are lift dimensions and path widths provided?
5. **Facilities Clarity:** Are toilets and quiet spaces detailed?
6. **Program Accommodations:** Does it cover hearing loops, captions, and tactile options?
7. **Transparency:** Does it honestly state what is **not** accessible?
8. **Format Quality:** Is it HTML-first and mobile-responsive?

## Add Your Example

Do you have a great building access guide? [Contribute it to our library!]({{ "/contribute/" | relative_url }})
