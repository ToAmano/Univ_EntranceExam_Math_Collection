import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import yaml from 'js-yaml';

let catalog;
export function readProblemGroups() {
  if (!catalog) catalog = yaml.load(readFileSync(resolve('..', 'data', 'problem_groups.yaml'), 'utf8'));
  return catalog;
}

/** Build cross-year recommendations from the curated group catalog. */
export function relatedProblemGroups(groups, currentId, entries) {
  const matchingGroups = groups.filter(group => [...group.problems, ...group.related].includes(currentId));
  if (!matchingGroups.length) return [];
  const solutions = new Map(entries
    .filter(entry => entry.data.type === 'solution')
    .map(entry => [
      `${entry.data.university}/${entry.data.category}/${entry.data.year}/${entry.data.question}`,
      entry.slug,
    ]));

  return matchingGroups.flatMap(group => {
    const items = [
      ...group.problems.map(id => ({ id, relation: 'same' })),
      ...group.related.map(id => ({ id, relation: 'related' })),
    ]
      .filter(item => item.id !== currentId && solutions.has(item.id))
      .map(item => ({ ...item, slug: solutions.get(item.id) }));
    return items.length ? [{ id: group.id, name: group.name, items }] : [];
  });
}
